from django.shortcuts import render

#from .models import Player

# Create your views here.


def game(request):
    return render(request, 'game.html', locals())
