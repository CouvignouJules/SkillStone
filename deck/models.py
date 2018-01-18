# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin


class CardType(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class CardTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = []
    ordering = ['id']
    fieldsets = [('nom', {
        'description': 'nom',
        'fields': ['name']
    })]


class Effect(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class EffectAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = []
    ordering = ['id']
    fieldsets = [('nom', {
        'description': 'nom',
        'fields': ['name']
    })]


class Card(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cost = models.IntegerField()
    attack = models.IntegerField()
    health = models.IntegerField()
    cardType = models.ForeignKey(CardType, on_delete=models.SET_NULL, blank=True, null=True)
    effect = models.ForeignKey(Effect, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name + str(self.cost)


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'cost', 'attack', 'health']
    search_fields = ['effect', 'cardType']
    list_filter = ['cost', 'cardType']
    ordering = ['id']
    fieldsets = [
        ('nom', {
            'description': 'nom',
            'fields': ['name', 'cardType', 'description']
        }),
        ('stat', {
            'description': 'stat',
            'fields': ['cost', 'attack', 'health', 'effect']
        })
    ]


class Deck(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cards = models.ManyToManyField(Card)

    def __str__(self):
        return self.name


class DeckAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['cards']
    list_filter = []
    ordering = ['id']
    fieldsets = [
        ('Deck', {
            'description': 'nom',
            'fields': ['name']
        }),
        ('Carte', {
            'description': 'carte',
            'fields': ['cards']
        })
    ]


class Player(models.Model):
    pseudo = models.CharField(max_length=30)
    life = models.IntegerField(default=30)
    hand = models.ManyToManyField(Card, related_name='card')
    deck = models.ForeignKey('Deck', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.pseudo


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['pseudo', 'life', 'deck']
    search_fields = ['deck']
    list_filter = []
    ordering = ['id']
    fieldsets = [
        ('player', {
            'description': 'player',
            'fields': ['pseudo']
        }),
        ('deck',{
            'description': 'deck',
            'fields': ['deck']
        })
    ]
