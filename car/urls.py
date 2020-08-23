from django.urls import path
from . import views

urlpatterns = [
        path("", views.all_cars_and_search),
        path("<int:id>", views.get_car_data),
        path("create/", views.create_car),
        path("edit_car/<int:id>", views.edit_car),
        path("del_car/<int:id>", views.del_car),
        ]
