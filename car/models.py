from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from . import choices
from django.contrib.auth.models import User
from django_random_queryset import RandomManager


class Car(models.Model):
    objects = RandomManager()
    category = models.CharField(max_length=30, choices=choices.CATEGORY, null=True)
    car_model = models.CharField(max_length=30, choices=choices.CAR_MODELS, null=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField(choices=choices.YEAR, null=True)
    price = models.IntegerField() #Գին
    running = models.IntegerField(validators=[MaxValueValidator(1000000), MinValueValidator(100)]) #Վազքը
    modification = models.CharField(max_length=100, blank=True, null=True) #Մոդիֆիկացիա
    shed = models.CharField(max_length=30, choices=choices.SHED, null=True) #Թափք
    transfer_box = models.CharField(max_length=30, choices=choices.TRANSFER_BOX, null=True) #Փոխանցման տուփ
    wheel = models.CharField(max_length=30, choices=(("Ձախ", "Ձախ"), ("Աջ", "Աջ")), null=True) #Ղեկ
    engine = models.CharField(max_length=30, choices=choices.ENGINE, null=True) #Շարժիչ
    color = models.CharField(max_length=30, choices=choices.COLOR, null=True) #Գույնը
    color_of_the_hall = models.CharField(max_length=30, choices=choices.COLOR, null=True) #Սրահի գույնը
    engine_capacity = models.CharField(choices=choices.ENGINE_CAPACITY, max_length=5, null=True) #Շարժիչի ծավալը
    horsepower = models.IntegerField() #Ձիաուժ
    cycling = models.IntegerField(validators=[MaxValueValidator(25), MinValueValidator(10)]) #Անվահեծերը
    picture = models.ImageField(upload_to='Pictures/', default='static_images/default.jpg')
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        x = "   "
        return str(self.car_model) + x + str(self.name) + x + str(self.year) + "   " + str(self.horsepower) + "HP"