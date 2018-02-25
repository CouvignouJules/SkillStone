# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from deck.models import Card
from deck.models import Player
from deck.models import Deck
from django.contrib.auth.models import User



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

"""
Partie déroulement du jeu.
Les données sont stockées en json dans la base de données pour le déroulement du jeu car cela modifierai sinon les
données existante et fixe, par example quand une carte perd de la vie.
Tables temporaire pour la durée de la partie évidemment.
"""
class GamePlayer(models.Model):
    name = models.CharField(max_length=30, default=None)
    hp = models.IntegerField(default=30)
    hand = models.TextField(default=None)
    deck = models.TextField(default=None)
    board = models.TextField(default=None)


    def __init__(self, name):
        super(GamePlayer, self).__init__()
        self.name = name
        self.hp = 30 # TODO : initialiser en fonction des regles
        self.hand = []
        self.board = []






class Game(models.Model):
    players = models.ManyToManyField(GamePlayer)



