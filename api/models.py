# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Building(models.Model):
    title = models.CharField(max_length=50)
    facilities = models.TextField(max_length=500)
    services = models.TextField(max_length=500)
    cant_pax = models.PositiveSmallIntegerField()
    daily_cost = models.FloatField()
    image = models.ImageField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    total_cost = models.FloatField()

    def __str__(self):
        return self.user + ' ' + self.building


class BookingDate(models.Model):
    date = models.DateField(auto_now=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=None)
    building = models.ForeignKey(Building, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.booking.user.email + ' - ' + self.building.title + ' - ' + self.date

