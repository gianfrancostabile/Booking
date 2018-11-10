# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import (
    Building,
    Booking,
    BookingDate
)
from django.shortcuts import render, redirect

# Create your views here.


def building_mapper(building):
    building.stars = range(building.stars)
    return building

def retrieve_all(request):
    buildings = map(building_mapper,Building.objects.all())
    return render(request, 'buildings_list.html', {'buildings': buildings})


def retrieve(request, building_id):
    building = building_mapper(Building.objects.get(pk=building_id))
    dates = BookingDate.objects.filter(building=building.pk, booking=None)

    return render(request, 'building_one.html', {'building': building, 'dates': dates, 'cant_pax': range(1, building.cant_pax)})


def retrieve_by_params(request):
    if request.method == "POST":
        city_name = request.POST.get("city_name")
        pax = int(request.POST.get("cant_pax"))
        begin_date = request.POST.get("begin_date")
        end_date = request.POST.get("end_date")

        if begin_date and end_date:
            booking_dates = BookingDate.objects.filter(date__range=(begin_date, end_date))
        else:
            booking_dates = BookingDate.objects.all()

        buildings = []
        flag = 1
        for booking_date in booking_dates:
            for building in buildings:
                if building.pk == booking_date.building.pk:
                    flag = 0
                    break
            if flag == 1:
                buildings.append(booking_date.building)
            else:
                flag = 1
        buildings = map(building_mapper, buildings)

        if city_name:
            buildings = filter(lambda obj: obj.city.name == city_name, buildings)

        if pax > 0:
            buildings = filter(lambda obj: obj.cant_pax >= pax, buildings)
    else:
        buildings = map(building_mapper, Building.objects.all())

    return render(request, "buildings_list.html", {'buildings': buildings})


def create_booking(request):
    if request.method == "POST":
        building_id = request.POST.get("building_id")
        cant_pax = request.POST.get("cant_pax")
        dates_pk = dict(request.POST)["dates"]

        building = Building.objects.get(pk=building_id)

        booking = Booking()
        booking.building = building
        booking.total_cost = building.daily_cost * float(cant_pax) * len(dates_pk)
        booking.save()

        for date_pk in dates_pk:
            booking_date = BookingDate.objects.get(pk=date_pk)
            booking_date.booking = booking
            booking_date.save(force_update=True)

    return redirect('/api/building/')
