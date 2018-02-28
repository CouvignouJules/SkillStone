
from channels import Group
from game.models import Game, GamePlayer
from django.db import models
from django.contrib import admin
from deck.models import Card
from deck.models import Player
from deck.models import Deck
from collections import OrderedDict
import json
import random as rand
from django.contrib.auth.models import User
from game.serializer import GamePlayerSerializer, GameSerializer
from collections import OrderedDict
from django.core.exceptions import ObjectDoesNotExist


import json


def ws_connect(message):
	# On doit stipuler que la connexion est acceptée
	message.reply_channel.send({"accept": True})
	# On abonne l'utilisateur à un groupe si il y a moin de 2 joueurs

	Group("player").add(message.reply_channel)

def ws_message(message):

	import json

	obj = json.loads(message.content['text'])

	# En fonction de l'action, modification côté serveur ... model par exemple
	if "action" not in obj:
		message.reply_channel.send({"text": 'JSON error'})
	else:
		if obj['action'] == 'join':
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'draw':
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI

		elif obj['action'] == 'put':
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI
		elif obj['action'] == 'attack':
			Group("player").send({'text': json.dumps(obj)}) # Va nous servir à update l'UI
		elif obj['action'] == 'pass':
			Group("player").send({'text': json.dumps(obj)})  # Va nous servir à update l'UI

		#elif obj['action'] == 'disconnect':





def ws_disconnect(message):
	# Désabonnement du groupe


	Group("player").discard(message.reply_channel)

"""
def handToJson(cards):
	data = {}
	for card in cards.all():
		data['cards'].append(cardToJson(card))
	return data


def deckToJson(deck):
	data = {}
	data['name'] = deck.name
	data['cards'] = []
	for card in deck.cards.all():
		data['cards'].append(cardToJson(card))
	return data


def cardToJson(card):
	data = {}
	data['name'] = card.name
	data['img'] = str(card.img)
	data['description'] = card.description
	data['cost'] = card.cost
	data['attack'] = card.attack
	data['health'] = card.health
	data['cardtype'] = card.cardtype.name
	if card.effect != None:
		data['effect'] = card.effect.name

	return data


def addPlayer(game, username):

    :param username: Username of the player
    :return: Game is full ?

	# if self.players.count() < 2: #TODO : à décommenter pour limiter la partie à 2 joueurs
	gamePlayer = GamePlayer(name=username)

	tableUser = User.objects.get(username=username)
	player = Player.objects.get(user=tableUser)  # Ne pas confondre player et gameplayer
	if (player.deckcollection.first() == None):
		print("Ce joueur n'a aucun deck")  # TODO : Prévoir l'accés impossible à la partie si on a pas de deck ...
		return
	else:
		gamePlayer.deck = deckToJson(player.deckcollection.first())
		rand.shuffle(gamePlayer.deck['cards'])

	for i in range(0, 5):  # Initialisation de la main du joueur
		gamePlayer.hand.append(gamePlayer.deck['cards'][0])
		gamePlayer.deck['cards'].remove(gamePlayer.deck['cards'][0])

	# Besoin de remettre en string pour passer dans la bdd, oupas?
	#gamePlayer.deck = str(gamePlayer.deck)
	#gamePlayer.hand = str(gamePlayer.hand)
	#gamePlayer.board = str(gamePlayer.board)

	gamePlayer.save()

	game.players.add(gamePlayer)
	print("Nombre de joueurs : ")
	print(game.players.count())
	game.save()
	return False


# else:
#    return True


def removePlayer(game, username):

    :param username:
    :return:

	game.players.get(name=username).remove()


def attack(game, username, c1, c2):

    :param username: Attacker
    :param c1: Attacker card index on board
    :param c2: Attacked card index on board
    :return: Dead cards / players ?


	data = {}
	data['c1'] = 0
	data['c2'] = 0
	data['playerHP'] = 0  # If playerHP != 0 and game isn't finished, that means no card has been attacked
	data['gameFinished'] = False

	p1 = game.players.get(name=username)
	p2 = game.players.get().exclude(name=username)

	card1 = p1.board.objects.get(c1)
	card2 = p2.board.objects.get(c2)

	# If attacked is not a card (a player)
	if not card2:
		p2.hp -= card1.attack
		if p2.hp < 1:
			data['gameFinished'] = True
		else:
			data['playerHP'] = p2.hp
	else:
		card1.health -= card2.attack
		card2.health -= card1.attack
		if card1.health < 1:
			p1.board.objects.remove(card1)
		else:
			data['c1'] = card1.health

		if card2.health < 1:
			p2.board.objects.remove(card2)
		else:
			data['c2'] = card2.health

	# TODO : tester fin partie, carte morte etc

	game.save()

	json_data = json.dumps(data)
	return json_data


def draw(game, username, number):

    :param username: Username of the drawer
    :param number: Amount of cards drawed
    :return: Hand is full ?


	handIsFull = False

	# print(self.players)
	print("Nombre de joueurs : ");
	print(game.players.count())

	# print(Game.objects.get(id=1).players.all())

	for i in range(0, number):
		handIsFull = playerDraw(game,username)

	game.save()

	return handIsFull


def put(game,username, card):

    :param username: Username of the player putting card
    :param card: Card put
    :return: Board == full ?


	boardIsFull = False

	p = game.players.objects.filter(name=username)

	if p.board.length < 8:
		game.board.add(card)
	else:
		boardIsFull = True

	game.save()

	return boardIsFull


def playerDraw(game, username):
	
    :return: Hand is full ?
    

	lol = GamePlayer.objects.all()
	print("wow")

	player = Game.objects.raw(
		'SELECT * FROM game_game_players ps,game_gameplayer p where ps.id = p.id AND name = %s limit 1', [username])
	data = GamePlayerSerializer(player, many=True).data
	print(data)

	data = json.dumps(data)
	data.replace('"[','[').replace(']"',']').replace('"{','{').replace('}"','}').replace('"',"'").replace('\\','')
	item_dict = json.loads(data)
	print(item_dict)
	print(type(item_dict))
	item_dict = item_dict[0]

	final = item_dict['hand']
	print(final)
	print(type(final))
	plz = final.replace('\'','"')
	mamain = json.loads(plz)

	finaldeck = item_dict['deck']
	print(finaldeck)
	print(type(finaldeck))
	print (finaldeck)
	print (type(finaldeck))
	finallol = finaldeck.split("[")[1][:-2]
	lastomg = "["+finallol.replace('\'','"')+"]"
	mondeck = json.loads(lastomg)

	print("avant")
	print(mamain)
	print(mondeck)

	if (len(mamain) < 11 ):
		mamain.append(mondeck[0])
	mondeck.pop(0)

	print("apres")
	print(mamain)
	print(mondeck)

	print("here")
	mamainfinale = str(mamain)
	mondeckfinale =  finaldeck.split("[")[0]+str(mondeck)+"}"
	#mamainfinale = mamainfinale.replace('\'','\\\'')
	#mondeckfinale = mondeckfinale.replace('\'','\\\'')
	print(mamainfinale)
	print(mondeckfinale)

	#lol = GamePlayer.objects.get(name=username)
	#lol.hand = mamainfinale
	#lol.deck = mondeckfinale
	#lol.save()

	
	requetemain = "UPDATE game_gameplayer SET hand = "+"\""+mamainfinale+"\""+"WHERE name = "+"\""+username+"\""
	print(requetemain)
	requetedeck = "UPDATE game_gameplayer SET deck = "+"\""+mondeckfinale+"\""+"WHERE name = "+"\""+username+"\""
	print(requetemain)

	player = Game.objects.raw(requetemain)
	player = Game.objects.raw(requetedeck)

	#for item in item_dict[0]:
		#print(item)

	#print(item_dict)
	#print(len(item_dict[0]['hand']))

	#data[0]['hand'].append(player.deck[0])

    if player.hand.length < 10:
        player.hand.append(player.deck[0])
        return True
    else:
        player.hand['card'].remove(player.deck[0])
        return False
    """
