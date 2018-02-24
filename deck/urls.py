from django.conf.urls import url, include
from rest_framework.authtoken import views as apiViews
from . import views

urlpatterns = [
    url(r'^$', views.myCollection, name='collection'),
    url(r'^/deck$', views.newDeck),
    url(r'^/deck/(?P<id>[0-9]+)$', views.deck),
    url(r'^/cardCollection$', views.cardCollection),
    url(r'^/cardCollection/(?P<user>[0-9]+)$', views.cardCollection),
    url(r'^/deckCollection$', views.deckCollection),
    url(r'^/deckCollection/(?P<user>[0-9]+)$', views.deckCollection),
    url(r'^/authenticate$', apiViews.obtain_auth_token)
]
