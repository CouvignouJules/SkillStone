from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.myCollection, name='collection'),
    url(r'^/deck$', views.deckList),
    url(r'^/deck/(?P<id>[0-9]+)$', views.deck),
    url(r'^/collection$', views.collection)
]
