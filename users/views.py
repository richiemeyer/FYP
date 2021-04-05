from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from . import models
from django.core import serializers
from .models import Profile
from django.contrib.gis.geos import Point
from django.template import RequestContext


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account has been created for {username}! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def update_location(request):
    try:
        print('in update location')
        user = request.user
        print(user)
        user_profile = models.Profile.objects.get(user__username=user)
        print(user_profile)
        if not user_profile:
            raise ValueError("Can't get User details")

        print('user_profile')
        print(user_profile)

        point = request.POST["point"]

        # point = [float(part) for part in point]
        # point = Point(point, srid=4326)

        print('point')
        print(point)

        user_profile.last_location = point
        user_profile.save()

        return JsonResponse({"message": f"Set location to {point})."}, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def get_last_journey(request):
    try:
        locations = serializers.serialize('python',
                                          Profile.objects.filter(user=request.user)[:10].only('last_location'))
        locations_json = [d['fields'] for d in locations]
        locations_json = [{k: v for k, v in d.items() if k != 'user'} for d in locations_json]
        print(locations_json)

        return JsonResponse(locations_json, safe=False, status=200)
    except Exception as e:
        return JsonResponse({"message": str(e)}, status=400)


def handler404(request, *args):
    response = render('error.html')
    response.status_code = 404
    return response
