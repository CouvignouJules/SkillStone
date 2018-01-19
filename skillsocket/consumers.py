from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group
from deck.models import Card
from deck.models import Player
from django.contrib.auth.models import User
from django.core.cache import caches
from django.core.cache import cache



def ws_connect(message):
	# On doit stipuler que la connexion est acceptée
	message.reply_channel.send({"accept": True})
	# On abonne l'utilisateur à un groupe si il y a moin de 2 joueurs
	#if Group("player").__sizeof__() < 2:
	Group("player").add(message.reply_channel)


def ws_message(message):

	import json

	obj = json.loads(message.content['text'])


	# En fonction de l'action, modification côté serveur ... model par exemple
	if "action" not in obj:
		message.reply_channel.send({"text": 'JSON error'})
	else:
		tableUser = User.objects.filter(username=obj['username'])
		player = Player.objects.filter(user=tableUser)

		if obj['action'] == 'join':
			# Que faire niveau backend ?


			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'draw':

			for i in range(1,obj['number']):
				player.Player.drawFromDeck()

			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'put':
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'attack':


			#attackingCard = Card.objects.filter(name=obj['attackingCard'])
			#target = Card.objects.filter(name=obj['target'])
			#if not target.exists(): #Sert à savoir si une carte est attaquée ou un joueur
			#	target = Player.objects.filter(pseudo=obj['target'])
			#	target.Player.setLife(target.Player.getLife() - attackingCard.Card.getAttack())

			#obj['lostHealth'] = attackingCard.getAttack()

			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI


			# Modification des points de vie de un tel
			# Vérification de fin de partie ou non




def ws_disconnect(message):
	# Désabonnement du groupe
	Group("player").discard(message.reply_channel)
