# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


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