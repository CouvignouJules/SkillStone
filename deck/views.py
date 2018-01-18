from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Deck, Card
from .serializer import DeckSerializer, CardSerializer


@login_required
def myCollection(request):
    return render(request, 'deck.html')


@api_view(['GET', 'POST'])
def deckList(request):
    if request.method == 'GET':
        decks = Deck.objects.all()
        serializer = DeckSerializer(decks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        postedData = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
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
def collection(request):
    collection = Card.objects.all()
    serializer = CardSerializer(collection, many=True)
    return Response(serializer.data)
