from django.conf.urls import url, include
from rest_framework.authtoken import views as apiViews
from . import views

urlpatterns = [
    url(r'^$', views.myCollection, name='collection'),
    url(r'^/deck$', views.deckList),
    url(r'^/deck/(?P<id>[0-9]+)$', views.deck),
    url(r'^/collection$', views.collection),
    url(r'^/collection/(?P<user>[0-9]+)$', views.collection),
    url(r'^/authenticate$', apiViews.obtain_auth_token)
]
