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
admin.site.register(Booking)


class BookingDateInline(admin.TabularInline):
    model = BookingDate
    fk_name = 'building'
    extra = 0


class AdminBuildingInline(admin.ModelAdmin):
    inlines = [BookingDateInline]


admin.site.register(Building, AdminBuildingInline)
