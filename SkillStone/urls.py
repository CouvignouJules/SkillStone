"""SkillStone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from HMAuth import views as hmauth_views
from deck import views as deck_views
from game import views as game_views
from SkillStone import views as skill_views


urlpatterns = [
    url(r'^$', hmauth_views.home, name='home'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', hmauth_views.signup, name='signup'),
    url(r'^accounts/profile/$', skill_views.profile, name='profile'),
    url(r'^deck/$', deck_views.deck, name='deck'),
    url(r'^game/$', game_views.game, name='game'),
    url(r'^admin/', admin.site.urls),

]
