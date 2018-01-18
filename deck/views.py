from django.shortcuts import render
import logging

from .models import Card
from .models import Player
# Create your views here.


def deck(request):
    logger = logging.getLogger(__name__)
    logger.info('test log deck')
    Cards = Card.objects.all()
    # TODO : get player from session and put his hand in a var
    #resultSet2 = Player.objects.first().hand
    return render(request, 'deck.html', locals())
