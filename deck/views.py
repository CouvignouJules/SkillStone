from django.shortcuts import render

from .models import Card
from .models import Player
# Create your views here.


def deck(request):
	Cards = Card.objects.all()
	#TODO : get player from session and put his hand in a var
	#resultSet2 = Player.objects.first().hand
	return render(request,'deck.html',locals())