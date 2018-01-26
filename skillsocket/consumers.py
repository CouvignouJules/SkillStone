
from channels import Group
from game.models import Game


def ws_connect(message):
	# On doit stipuler que la connexion est acceptée
	message.reply_channel.send({"accept": True})
	# On abonne l'utilisateur à un groupe si il y a moin de 2 joueurs

	Group("player").add(message.reply_channel)

def ws_message(message):

	import json

	obj = json.loads(message.content['text'])

	game = Game.objects.first()

	# En fonction de l'action, modification côté serveur ... model par exemple
	if "action" not in obj:
		message.reply_channel.send({"text": 'JSON error'})
	else:
		if obj['action'] == 'join':
			# Que faire niveau backend ?
			if game == None:
				game = Game.objects.create()
			obj['gameIsFull'] = game.addPlayer(obj['username'])
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'draw':
			game.draw(obj['username'],obj['number'])
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'put':
			game.put(obj['username'],obj['card'])
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI
		elif obj['action'] == 'attack':
			game.attack(obj['username'],obj['attackingCard'],obj['target'])
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'disconnect':
			game.removePlayer(obj['username'])

		# Modification des points de vie de un tel
		# Vérification de fin de partie ou non




def ws_disconnect(message):
	# Désabonnement du groupe

	# TODO: prévoir la suppression de la game quelque part
	# Game.objects.all().delete()


	Group("player").discard(message.reply_channel)
