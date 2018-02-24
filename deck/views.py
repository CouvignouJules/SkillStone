from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from .models import Deck, Card
from .serializer import DeckSerializer, CardSerializer


@login_required
def myCollection(request):
    token = request.user.auth_token
    cards = Card.objects.all()
    cardCollection = getcollection(request.user.id)
    return render(request, 'deck.html', locals())


@api_view(['GET', 'POST'])
def deckList(request):
    if request.method == 'GET':
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        postedData = {
            'name': request.data.get('name'),
            'cards': request.data.get('cards')
        }
        serializer = DeckSerializer(data=postedData)
        if serializer.is_valid():
            serializer.save()
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
def collection(request, user=None):
    return Response(getcollection(user))


def getcollection(user):
    if user:
        collection = Card.objects.raw('SELECT * FROM deck_player_cardcollection LEFT JOIN deck_card ON deck_player_cardcollection.card_id = deck_card.id WHERE (deck_player_cardcollection.player_id = %s)',[user])
    else:
        collection = Card.objects.all()
    serializer = CardSerializer(collection, many=True)
    return serializer.data