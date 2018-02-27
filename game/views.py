from django.shortcuts import render
from deck import views
from django.contrib.auth.decorators import login_required
#from .models import Player

# Create your views here.

@login_required
def game(request):
    token = request.user.auth_token

    return render(request, 'game.html', locals())
