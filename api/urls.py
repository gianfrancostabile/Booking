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
import views


urlpatterns = [
    url(r'^building/$', views.retrieve_all, name='buildings_list'),
    url(r'^building/(?P<building_id>\d+)$', views.retrieve, name='building_one'),
    url(r'^building/filter/$', views.retrieve_by_params, name='building_filter'),
    url(r'^booking/$', views.create_booking, name='booking_create'),
]
