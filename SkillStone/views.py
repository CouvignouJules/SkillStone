from django.contrib.auth.decorators import login_required
from django.shortcuts import render


# vue de menu de l'aplication permetant de naviguer entre toutes les applications
@login_required
def profile(request):
    return render(request, 'profile.html')
