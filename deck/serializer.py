from rest_framework import serializers
from .models import Deck,Card

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        exclude = []

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = []
