from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Deck, Card
from .serializer import DeckSerializer, CardSerializer


@login_required
def myCollection(request):
    token = request.user.auth_token

    cards = getCardCollection()
    cardCollection = getCardCollection(request.user.id)

    decks = getDeckCollection()
    deckCollection = getDeckCollection(request.user.id)

    return render(request, 'deck.html', locals())


@api_view(['POST'])
def newDeck(request):
    postedData = {
        'name': request.data.get('name'),
        'cards': request.data.get('cards')
    }
    serializer = DeckSerializer(data=postedData)
    if serializer.is_valid():
        serializer.save()
        request.user.player.deckcollection.add(serializer.data["id"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'DELETE'])
def deck(request, id=None):
    if request.method == 'GET':
        deck = Deck.objects.get(id=id)
        serializer = DeckSerializer(deck, many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        deck = Deck.objects.get(id=id)
        deck.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def cardCollection(request, user=None):
    return Response(getCardCollection(user))


def getCardCollection(user=None):
    if user:
        collection = Card.objects.raw('SELECT * FROM deck_player_cardcollection LEFT JOIN deck_card ON deck_player_cardcollection.card_id = deck_card.id WHERE (deck_player_cardcollection.player_id = %s)',[user])
    else:
        collection = Card.objects.all()
    serializer = CardSerializer(collection, many=True)
    return serializer.data


@api_view(['GET'])
def deckCollection(request, user=None):
    return Response(getDeckCollection(user))


def getDeckCollection(user=None):
    if user:
        collection = Deck.objects.raw('SELECT * FROM deck_player_deckcollection LEFT JOIN deck_deck ON deck_player_deckcollection.deck_id = deck_deck.id WHERE (deck_player_deckcollection.player_id = %s)',[user])
    else:
        collection = Deck.objects.all()
    serializer = DeckSerializer(collection, many=True)
    return serializer.data