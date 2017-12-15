from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Player, Card
from .serializer import PlayerSerializer, CardSerializer

# Create your views here.


@api_view(['GET', 'VIEW'])
def cardAttackCard(request):
    if request.method == 'GET':
        card = Card.objects.all()
        serializer = CardSerializer(card, many=False)
        return Response(serializer.data)
    elif request.method == 'POST':
        postedData = {
            'attack': request.data.get('attack'),
            'health': request.data.get('health'),
            'cardType': request.data.get('cardType'),
            'effect': request.data.get('effect')
        }
        serializer = CardSerializer(data=postedData)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
