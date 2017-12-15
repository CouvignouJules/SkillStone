from django.db import models

# Create your models here.


class Player(models.Model):
    pseudo = models.CharField(max_length=30)
    life = models.IntegerField(default=30)
    hand = models.ManyToManyField(Card, related_name='hand')
    deck = models.ManyToManyField(Card, related_name='deck')

    def setLife(self, life):
        self.life = life
