from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth.models import User, Group


# @login_required
def home(request):

    return render(request, 'world/home.html')


def about(request):
    return render(request, 'world/about.html', {'title': 'About'})



