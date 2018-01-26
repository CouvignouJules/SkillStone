# -*- coding: utf-8 -*-
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import json


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
    img = models.ImageField(upload_to='static/img/card', default='static/img/card/deck.jpg')
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
            'fields': ['name', 'img', 'cardType', 'description']
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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cardCollection = models.ManyToManyField(Card, related_name='cardCollection')
    deckCollection = models.ManyToManyField(Deck, related_name='deckCollection')

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Player.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.player.save()


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['user']
    search_fields = ['deck']
    list_filter = []
    ordering = ['id']
    fieldsets = [
        ('Profile', {
            'description': 'Profile',
            'fields': ['user']
        }),
        ('deck',{
            'description': 'deck',
            'fields': ['cardCollection', 'deckCollection']
        })
    ]
