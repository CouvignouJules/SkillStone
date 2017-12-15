from django.db import models

# Create your models here.


class CardType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Effect(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    cost = models.IntegerField()
    attack = models.IntegerField()
    health = models.IntegerField()
    cardType = models.ForeignKey(CardType, on_delete=models.CASCADE)
    effect = models.ManyToManyField(Effect)


class Player(models.Model):
    pseudo = models.CharField(max_length=30)
    life = models.IntegerField(default=30)
    hand = models.ManyToManyField(Card, related_name='hand')
    deck = models.ManyToManyField(Card, related_name='deck')

    def setLife(self, life):
        self.life = life
