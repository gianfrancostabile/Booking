# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView
)
from django.core.urlresolvers import reverse_lazy
from .models import (
    City,
    Building,
    Booking
)
# Create your views here.


# -------------------------- City ------------------------------------ #
#
#
# class CityCreate(CreateView):
#     model = City
#     success_url = reverse_lazy('cities:list')
#     fields = ['name']
#
#
# class CityUpdate(UpdateView):
#     model = City
#     success_url = reverse_lazy('cities:list')
#     fields = ['name']
#
#
# class CityDelete(DeleteView):
#     model = City
#     success_url = reverse_lazy('cities:list')
#
#
# class CityList(ListView):
#     model = City
#
#
# class CityDetail(DetailView):
#     model = City
#

# -------------------------- BUILDING ------------------------------------ #


# class BuildingCreate(CreateView):
#     model = Building
#     success_url = reverse_lazy('buildings:list')
#     fields = ['title', 'facilities', 'services', 'cant_pax', 'begin_date', 'end_date', 'daily_cost', 'image', 'city']
#
#
# class BuildingUpdate(UpdateView):
#     model = Building
#     success_url = reverse_lazy('buildings:list')
#     fields = ['title', 'facilities', 'services', 'cant_pax', 'begin_date', 'end_date', 'daily_cost', 'image', 'city']
#
#
# class BuildingDelete(DeleteView):
#     model = Building
#     success_url = reverse_lazy('buildings:list')
#

class BuildingList(ListView):
    model = Building


class BuildingDetail(DetailView):
    model = Building


# -------------------------- Booking ------------------------------------ #
#
#
# class BookingCreate(CreateView):
#     model = Booking
#     success_url = reverse_lazy('bookings:list')
#     fields = ['user', 'building']
#
#
# class BookingUpdate(UpdateView):
#     model = Booking
#     success_url = reverse_lazy('bookings:list')
#     fields = ['user', 'building']
#
#
# class BookingDelete(DeleteView):
#     model = Booking
#     success_url = reverse_lazy('bookings:list')
#
#
# class BookingList(ListView):
#     model = Booking
#
#
# class BookingDetail(DetailView):
#     model = Booking
#
#
