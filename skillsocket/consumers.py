from django.http import HttpResponse
from channels.handler import AsgiHandler
from channels import Group


def ws_connect(message):
	# On doit stipuler que la connexion est acceptée
	message.reply_channel.send({"accept": True})
	# On abonne l'utilisateur à un groupe si il y a moin de 2 joueurs
	#if Group("player") < 2
	Group("player").add(message.reply_channel)

def ws_message(message):

	import json

	obj = json.loads(message.content['text'])


	#debug
	#print(message.content['text'])

	if "action" not in obj:
		message.reply_channel.send({"text": 'JSON error'})

	elif obj['action'] == 'join':
		Group("player").send({
			"text": "* " + obj['username'] + " a rejoint la partie",
		})


"""
	elif obj['action'] == 'draw':

	elif obj['action'] == 'attack':

	elif obj['action'] == 'draw':

	elif obj['action'] == 'draw':

	#...
"""

def ws_disconnect(message):
	# Désabonnement du groupe
	Group("player").discard(message.reply_channel)
