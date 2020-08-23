from django.shortcuts import render
from .models import Car
from .forms import CarForm
from .forms import EditCarForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator


def auth_username(request):
    auth_user_name = request.user
    return auth_user_name


def all_cars_and_search(request):
    cars = get_all_cars()
    if "q" in request.GET:
        cars = search(request, cars)
    if "year_min" in request.GET and "year_max" in request.GET:
        cars = search_cars_by_year(request, cars)
    if "min" in request.GET and "max" in request.GET:
        cars = price(request, cars)
    if "wheel_left" in request.GET or "wheel_right" in request.GET:
        cars = checkbox_wheel(request)
    paginator = Paginator(cars, 4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "car/all_cars.html", {"page_obj": page_obj,
                                                 "q": request.GET.get("q"),
                                                 "year_min": request.GET.get("year_min"),
                                                 "year_max": request.GET.get("year_max"),
                                                 "min": request.GET.get("min"),
                                                 "max": request.GET.get("max"),
                                                 "auth_username": auth_username(request), })


def get_all_cars():
    cars = Car.objects.all()
    return cars


def search(request, cars):
    if request.GET["q"]:
        cars = cars.filter(car_model__icontains=request.GET["q"])
    return cars


def search_cars_by_year(request, cars):
    if "year_min" in request.GET and "year_max" in request.GET:
        if request.GET.get("year_min") and request.GET.get("year_max"):
            cars = cars.filter(year__range=(request.GET["year_min"], request.GET["year_max"]))
        else:
            if request.GET["year_min"]:
                cars = cars.filter(year__gte=request.GET['year_min'])
            if request.GET["year_max"]:
                cars = cars.filter(year__lte=request.GET['year_max'])
    return cars


def price(request, cars):
    if "min" in request.GET and "max" in request.GET:
        if request.GET.get("min") and request.GET.get("max"):
            cars = cars.filter(price__range=(request.GET["min"], request.GET["max"]))
        else:
            if request.GET["min"]:
                cars = cars.filter(price__gte=request.GET['min'])
            if request.GET["max"]:
                cars = cars.filter(price__lte=request.GET['max'])
    return cars


def get_car_data(request, id):
    car = Car.objects.get(id=id)
    return render(request, 'car/car_data.html', {'car': car, "auth_username": auth_username(request)})


def checkbox_wheel(request):
    if "wheel_left" in request.GET or "wheel_right" in request.GET:
        if request.GET.get("wheel_left"):
            cars = Car.objects.filter(wheel="Ձախ")
        else:
            cars = Car.objects.filter(wheel="Աջ")
    return cars


# def create_car(request):
#     if request.method == "POST":
#         form = CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             Car.author = auth_username(request)
#             print("Y+Y+Y+Y+Y+Y+Y+Y", Car.author)
#             form.save()
#             print("Y+Y+Y+Y+Y+Y+Y+Y", Car.author)
#             return HttpResponseRedirect('/')
#     else:
#         form = CarForm()
#     return render(request, "car/create_car.html", {"form": form, "auth_username": auth_username(request)})


@login_required
def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car_obj = form.save()
            car_obj.author = auth_username(request)
            car_obj.save()
            return HttpResponseRedirect('/account/user_page')
    else:
        form = CarForm()
    return render(request, "car/create_car.html", {"form": form, "auth_username": auth_username(request)})


@login_required
def edit_car(request, id):
    car = Car.objects.get(id=id)
    if request.method == 'POST':
        form = EditCarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/user_page')
    else:
        form = EditCarForm(instance=car)
    return render(request, 'car/edit_car.html', {"form": form})


@login_required
def del_car(request, id):
    car = Car.objects.get(id=id)
    car.delete()
    return HttpResponseRedirect('/account/user_page')