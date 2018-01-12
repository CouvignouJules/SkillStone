from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group

def ws_connect(message):
	# On doit stipuler que la connexion est acceptée
	message.reply_channel.send({"accept": True})
	# On abonne l'utilisateur à un groupe si il y a moin de 2 joueurs
	if Group("player").__sizeof__() < 2:
		Group("player").add(message.reply_channel)

def ws_message(message):

	import json

	obj = json.loads(message.content['text'])


"""
	# En fonction de l'action, modification côté serveur ... model par exemple
	if "action" not in obj:
		message.reply_channel.send({"text": 'JSON error'})
	elif obj['action'] == 'join':
		# Insertion du nouveau joueur en base de données
	elif obj['action'] == 'draw':
		# Modification de la main joueur 2 en base de données ?
	elif obj['action'] == 'put':
		# Modification des cartes posées sur le terrain en base de données
	elif obj['action'] == 'attack':
		# Modification des points de vie de un tel
		# Vérification de fin de partie ou non

"""


def ws_disconnect(message):
	# Désabonnement du groupe
	Group("player").discard(message.reply_channel)
