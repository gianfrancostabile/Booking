"""buildings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from .views import (
    CityCreate,
    CityUpdate,
    CityDelete,
    CityList,
    CityDetail,
    BuildingCreate,
    BuildingUpdate,
    BuildingDelete,
    BuildingList,
    BuildingDetail,
    BookingCreate,
    BookingUpdate,
    BookingDelete,
    BookingList,
    BookingDetail
)


urlpatterns = [
    url(r'^city/$', CityList.as_view(), name='cityList'),
    url(r'^city/(?P<pk>\d+)$', CityDetail.as_view(), name='cityDetail'),
    url(r'^city/create$', CityCreate.as_view(), name='cityCreate'),
    url(r'^city/update/(?P<pk>\d+)$', CityUpdate.as_view(), name='cityUpdate'),
    url(r'^city/delete/(?P<pk>\d+)$', CityDelete.as_view(), name='cityDelete'),
    url(r'^building/$', BuildingList.as_view(), name='buildingList'),
    url(r'^building/(?P<pk>\d+)$', BuildingDetail.as_view(), name='buildingDetail'),
    url(r'^building/create$', BuildingCreate.as_view(), name='buildingCreate'),
    url(r'^building/update/(?P<pk>\d+)$', BuildingUpdate.as_view(), name='buildingUpdate'),
    url(r'^building/delete/(?P<pk>\d+)$', BuildingDelete.as_view(), name='buildingDelete'),
    url(r'^booking/$', BookingList.as_view(), name='bookingList'),
    url(r'^booking/(?P<pk>\d+)$', BookingDetail.as_view(), name='bookingDetail'),
    url(r'^booking/create$', BookingCreate.as_view(), name='bookingCreate'),
    url(r'^booking/update/(?P<pk>\d+)$', BookingUpdate.as_view(), name='bookingUpdate'),
    url(r'^booking/delete/(?P<pk>\d+)$', BookingDelete.as_view(), name='bookingDelete'),
]
