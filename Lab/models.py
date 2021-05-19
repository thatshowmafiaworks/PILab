from django.db import models
from django.contrib.auth.models import BaseUserManager


class Customer(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Plane(models.Model):
    city_from = models.CharField(max_length=30)
    city_to = models.CharField(max_length=30)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    landing_date = models.DateField()
    landing_time = models.TimeField()

    def __str__(self):
        return self.city_from + "->" + self.city_to


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.customer.__str__() + "-" + self.plane.__str__()

