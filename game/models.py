# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from deck.models import Card
from deck.models import Player
from deck.models import Deck
from collections import namedtuple
from random import *
from django.contrib.auth.models import User
import json

class Rules(models.Model):
    playersHP = models.IntegerField(default=30)     # Nombre de points de vie de chaque joueur
    startingHand = models.IntegerField(default=3)   # Nombre de cartes dans la main du joueur au début de la game
    spellUse = models.BooleanField(default=True)    # Autorisation d'utiliser les sorts ou non
    monstersBoard = models.IntegerField(default=7)  # Nombre de monstres autorisés sur chaque plateau

class RulesAdmin(admin.ModelAdmin):
    list_display = ['playersHP', 'startingHand', 'spellUse', 'monstersBoard']
    list_filter = ['playersHP', 'startingHand']
    ordering = ['playersHP']
    fieldsets = [
        ('Players relative', {
            'description': 'HP & hand',
            'fields': ['playersHP', 'startingHand']
        }),
        ('Game relative', {
            'description': 'Spell & monsters',
            'fields': ['spellUse', 'monstersBoard']
        })
    ]


# TODO : TOUT TESTER


class GamePlayer(models.Model):
    name = models.CharField(max_length=30)
    hp = models.IntegerField(default=30)
    hand = models.ManyToManyField(Card, related_name='hand')
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    board = models.ManyToManyField(Card, related_name='board')

    def __init__(self, name):
        self.hp = 30 # TODO : initialiser en fonction des regles

class Game(models.Model):
    players = models.ManyToManyField(GamePlayer)

    def __init__(self):
        self.addPlayer(username="toto")
        pass
        #GamePlayer.objects.all().delete()

    def addPlayer(self, username):
        """
        :param username: Username of the player
        :return: True if game wasn't full, false if it was full
        """
        if self.players.count() < 2:
            s = GamePlayer(name=username)
            tableUser = User.objects.filter(username=username)
            player = Player.objects.filter(user=tableUser)
            s.deck = player.deckCollection.first()
            for i in range(0, 5):
                s.hand.add(s.deck.cards[random.uniform(0, s.deck.cards.length)])
            self.save()
            return True
        else:
            return False

    def attack(self, username, c1, c2):
        """
        :param username: Attacker
        :param c1: Attacker card index on board
        :param c2: Attacked card index on board
        :return: Dead cards / players ?
        """

        data = {}
        data['c1'] = 0
        data['c2'] = 0
        data['playerHP'] = 0 # If playerHP != 0 and game isn't finished, that means no card has been attacked
        data['gameFinished'] = False


        p1 = self.players.objects.filter(name=username)
        p2 = self.players.objects.filter().exclude(name=username)

        card1 = p1.board.objects.get(c1)
        card2 = p2.board.objects.get(c2)

        # If attacked is not a card (a player)
        if not card2:
            p2.hp -= card1.attack
            if p2.hp < 1:
                data['gameFinished'] = True
            else:
                data['playerHP'] = p2.hp
        else:
            card1.health -= card2.attack
            card2.health -= card1.attack
            if card1.health < 1:
                p1.board.objects.remove(card1)
            else:
                data['c1'] = card1.health

            if card2.health < 1:
                p2.board.objects.remove(card2)
            else:
                data['c2'] = card2.health


        # TODO : tester fin partie, carte morte etc

        self.save()


        json_data = json.dumps(data)
        return json_data


    def draw(self, username, number):
        """
        :param username: Username of the drawer
        :param number: Amount of cards drawed
        :return: Hand == full ?
        """

        handIsFull = False

        p = self.players.objects.filter(name=username)

        for i in range(0, number):
            indexRandCard = random.uniform(0, p.deck.length)
            if p.hand.length < 10:
                p.hand.add(p.deck[indexRandCard])
            else:
                p.deck.remove(indexRandCard)
                handIsFull = True

        self.save()

        return handIsFull


    def put(self, username, card):
        """
        :param username: Username of the player putting card
        :param card: Card put
        :return: Board == full ?
        """

        boardIsFull = False


        p = self.players.objects.filter(name=username)

        if p.board.length < 8:
            self.board.add(card)
        else:
            boardIsFull = True

        self.save()

        return boardIsFull


