# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from deck.models import Card
from deck.models import Player
from deck.models import Deck
from collections import namedtuple
import random as rand
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
    name = models.CharField(max_length=30, default=None)
    hp = models.IntegerField(default=30)
    hand = models.TextField(max_length=1000, default=None) # CharField max max_length = 255
    deck = models.TextField(max_length=50000, default=None)
    board = models.TextField(max_length=1000, default=None)

    def __init__(self, name):
        super(GamePlayer, self).__init__()
        self.name = name
        self.hp = 30 # TODO : initialiser en fonction des regles
        self.hand = []
        self.board = []


    def draw(self):
        """
        :return: Hand is full ?
        """
        if self.hand.length < 10:
            self.addHand(self.deck[0])
            return True
        else:
            self.removeHand(self.deck[0])
            return False

    def addHand(self,card):
        self.hand.append(card)

    def removeHand(self, card):
        self.hand['card'].remove(card)

    def addDeck(self, card):
        self.deck.append(card)

    def removeDeck(self, card):
        self.deck['cards'].remove(card)

    def shuffleDeck(self):
        rand.shuffle(self.deck['cards'])




class Game(models.Model):
    players = models.ManyToManyField(GamePlayer)

    #def __init__(self):
    #    super(self).__init__()
    #    GamePlayer.objects.all().delete()

    def handToJson(self,cards):
        data = {}
        for card in cards.all():
            data['cards'].append(Game.cardToJson(self,card))
        return data

    def deckToJson(self,deck):
        data = {}
        data['name'] = deck.name
        data['description'] = deck.description
        data['cards'] = []
        for card in deck.cards.all():
            data['cards'].append(Game.cardToJson(self,card))
        return data


    def cardToJson(self,card):
        data = {}
        data['name'] = card.name
        data['img'] = str(card.img)
        data['description'] = card.description
        data['cost'] = card.cost
        data['attack'] = card.attack
        data['health'] = card.health
        data['cardType'] = card.cardType.name
        if card.effect != None:
            data['effect'] = card.effect.name

        return data

    def addPlayer(self, username):
        """
        :param username: Username of the player
        :return: Game is full ?
        """
        if self.players.count() < 2:
            gamePlayer = GamePlayer(name=username)

            tableUser = User.objects.get(username=username)
            player = Player.objects.get(user=tableUser)
            print(player.deckCollection)
            gamePlayer.deck = self.deckToJson(player.deckCollection.first())

            gamePlayer.shuffleDeck()

            for i in range(0, 5):  # Initialisation de la main du joueur
                gamePlayer.addHand(gamePlayer.deck['cards'][0])
                gamePlayer.removeDeck(gamePlayer.deck['cards'][0])


            gamePlayer.save() # TODO : fix : django.db.utils.DataError: (1406, "Data too long for column 'deck' at row 1")
            self.players.add(gamePlayer)
            self.save()
            return False
        else:
            return True


    def removePlayer(self, username):
        """
        :param username:
        :return:
        """
        self.players.get(name=username).remove()

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


        p1 = self.players.get(name=username)
        p2 = self.players.get().exclude(name=username)

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
        :return: Hand is full ?
        """

        handIsFull = False

        player = self.players.get(name=username)

        for i in range(0, number):
            handIsFull = player.draw()

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


