# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import datetime

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
    stars = models.PositiveSmallIntegerField(max_length=1, default=1)
    daily_cost = models.FloatField()
    image = models.ImageField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Booking(models.Model):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    total_cost = models.FloatField()

    def __str__(self):
        return self.building + ' ' + self.total_cost


class BookingDate(models.Model):
    date = models.DateField(auto_now=False, default=now)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.building.title + ' - ' + self.date

