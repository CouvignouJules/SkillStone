from django.db import models
from django.contrib import admin


class CardType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class CardTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    ordering = ['name']

    fieldsets = (
        (
            'Général', {
                'description': 'Création d\'un type de carte',
                'fields': ['name']
            }
        )
    )


class Effect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class EffectAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    ordering = ['name']

    fieldsets = (
        (
            'Général', {
                'description': 'Création d\'un effet',
                'fields': ['name']
            }
        )
    )


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cost = models.IntegerField()
    attack = models.IntegerField()
    health = models.IntegerField()
    cardType = models.ForeignKey(CardType, on_delete=models.CASCADE)
    effect = models.ManyToManyField(Effect)


class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost', 'attack', 'health', 'cardType', 'effect']
    list_filter = ['name', 'cost', 'attack', 'health', 'cardType']
    ordering = ['id']

    fieldsets = (
        (
            'Mise en forme', {
                'description': 'Réglages communs',
                'fields': ['name', 'cost', 'cardType', 'description']
            }
        ),
        (
            'Spécificité monstre', {
                'description': 'Création d\'une carte monstre',
                'fields': ['attack', 'health', 'effect']
            }
        ),
        (
            'Spécificité sort', {
                'description': 'Création d\'une carte sort',
                'fields': ['effect']
            }
        )
    )


class Player(models.Model):
    pseudo = models.CharField(max_length=30)
    life = models.IntegerField(default=30)
    hand = models.ManyToManyField(Card, related_name='hand')
    deck = models.ManyToManyField(Card, related_name='deck')

    def setLife(self, life):
        self.life = life

    def setPseudo(self, pseudo):
        if pseudo.length() > 0:
            self.pseudo = pseudo

    def addCardToHand(self, card):
        if hand.count() < 11:
            self.hand.add(card)

    def addCardToDeck(self, card):
        if deck.count() < 31:
            self.deck.add(card)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['pseudo', 'life', 'hand', 'deck']
    list_filter = ['pseudo', 'life']
    ordering = ['pseudo']

    fieldsets = (
        (
            'Création d\'un joueur', {
                'description': 'Données du joueur',
                'fields': ['pseudo', 'life', 'hand', 'deck']
            }
        )
    )
# Create your models here.
