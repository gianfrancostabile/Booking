# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=50)


class Building(models.Model):
    title = models.CharField(max_length=50)
    facilities = models.CharField(max_length=500)
    services = models.CharField(max_length=500)
    cant_pax = models.PositiveSmallIntegerField()
    begin_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    daily_cost = models.FloatField()
    image = models.ImageField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    total_cost = models.FloatField()
