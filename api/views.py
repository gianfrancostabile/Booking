# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import (
    City,
    Building,
    BookingDate
)
# Create your views here.


def retrieve_all(request):
    buildings = Building.objects.all()
    return buildings


def retrieve(request, building_id):
    buildings = Building.objects.get(pk=building_id)
    return buildings


def retrieve_by_params(request, city_name, start_date, end_date):
    buildings = []
    booking_dates = BookingDate.objects.filter(date__range=(start_date, end_date))
    for db in booking_dates:
        if db.city.name == city_name:
            buildings.append(db)

    return buildings


