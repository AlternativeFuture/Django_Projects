from django.shortcuts import render
from car.models import Car


def auth_username(request):
    auth_user_name = request.user
    return auth_user_name


def home_page(request):
    cars = Car.objects.filter()
    cars4 = cars.random(4)
    return render(request, "index.html", {"cars4": cars4, "auth_username": auth_username(request)})


