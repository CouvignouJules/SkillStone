from rest_framework import serializers
from .models import GamePlayer,Game

class GamePlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamePlayer
        exclude = []

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = []
