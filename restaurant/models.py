from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model

class MenuItem(models.Model):
    title = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory = models.PositiveIntegerField(default=0)

class Booking(models.Model):
    name = models.CharField(max_length=120)
    no_of_guests = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_time = models.TimeField()
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

