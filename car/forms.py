from django import forms
from .models import Car
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["category", "car_model", "name", "year",
                  "price", "running", "modification",
                  "shed", "transfer_box", "wheel", "engine",
                  "color", "color_of_the_hall", "engine_capacity",
                  "horsepower", "cycling", "picture"]


class EditCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ["category", "car_model", "name", "year",
                  "price", "running",
                  "shed", "transfer_box", "wheel", "engine",
                  "color", "color_of_the_hall", "engine_capacity",
                  "horsepower", "cycling", "picture"]


# class SignupForm(UserCreationForm):
#     email = forms.EmailField(max_length=200, help_text='Required')
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')





