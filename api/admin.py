# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import (
    City,
    Building,
    Booking,
    BookingDate
)

# Register your models here.
admin.site.register(City)
admin.site.register(Building)
admin.site.register(Booking)
admin.site.register(BookingDate)