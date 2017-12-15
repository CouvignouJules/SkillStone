from rest_framework import serializers
from .models import Player, Card


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        exclude = []


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        exclude = []
