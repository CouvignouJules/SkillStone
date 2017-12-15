from django.shortcuts import render

from .models import Player

# Create your views here.


def game(request):
    Players = Player.objects.all()
    return render(request, 'game.html', locals())
