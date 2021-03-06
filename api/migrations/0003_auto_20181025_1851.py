# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 21:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20181019_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingDates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Booking')),
            ],
        ),
        migrations.RemoveField(
            model_name='building',
            name='begin_date',
        ),
        migrations.RemoveField(
            model_name='building',
            name='end_date',
        ),
        migrations.AddField(
            model_name='bookingdates',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Building'),
        ),
    ]
