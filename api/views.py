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
    return render(request, 'template.html', {'buildings': buildings})


def retrieve(request, building_id):
    building = Building.objects.get(pk=building_id)
    return render(request, 'template.html', {'building': building})


def retrieve_by_params(request):
    buildings = []
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
            # for db in booking_dates:
            #     if db.city.name == city_name:
            #         buildings.append(db)

    return render(request, "template.html", {'buildings': buildings})


def create_booking(request):
    if request.method == "POST":
        building_id = request.POST.get("building_id")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")

        building = Building.objects.get(pk=building_id)
        booking = Booking()
        booking.building = building
        booking.total_cost = (end_date - start_date).days

    return render(request, "template.html")