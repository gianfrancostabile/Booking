# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdate',
            name='booking',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.Booking'),
        ),
    ]
