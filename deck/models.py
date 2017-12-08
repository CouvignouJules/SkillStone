from django.db import models





class CardType(models.Model)
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)


class Effect(models.model)
	id models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)


class Card(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	cost = models.IntegerField()
	attack = models.IntegerField()
	health = models.IntegerField()
	cardType = models.ForeignKey(CardType, on_delete=models.CASCADE)
	effect = models.ManyToMany(Effect)


class Player(models.Model):
	pseudo = models.CharField(max_length=30)
	life = models.IntegerField(default=30)
	hand = models.ManyToManyField(Card)
	deck = models.ManyToManyField(Card)

	def setLife(self, life):
		self.life = life

	def setPseudo(self, pseudo):
		if pseudo.length() > 0
			self.pseudo = pseudo

	def addCardToHand(self, card):
		if hand.count() < 11
			self.hand.add(card)

	def addCardToDeck(self, card):
		if deck.count() < 31
			self.deck.add(card)


# Create your models here.
