# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import (
    City,
    Building,
    Booking,
    BookingDate
)
from django.shortcuts import render

# Create your views here.


def retrieve_all(request):
    buildings = Building.objects.all()
    return render(request, 'buildings_list.html', {'buildings': buildings})


def retrieve(request, building_id):
    building = Building.objects.get(pk=building_id)
    dates = BookingDate.objects.filter(building=building.pk, booking=None)
    return render(request, 'building_one.html', {'building': building, 'dates': dates})


def retrieve_by_params(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        if start_date and end_date:
            booking_dates = BookingDate.objects.filter(date__range=(start_date, end_date))
        else:
            booking_dates = BookingDate.objects.all()

        buildings = map(lambda obj: obj.city, booking_dates)

        if city_name:
            buildings = filter(lambda obj: obj.name == city_name, buildings)
    else:
        buildings = Building.objects.all()

    return render(request, "buildings_list.html", {'buildings': buildings})


def create_booking(request):
    if request.method == "POST":
        building_id = request.POST.get("building_id")
        dates = request.POST.get("dates")

        building = Building.objects.get(pk=building_id)
        booking = Booking()
        booking.building = building

    return render(request, "template.html")