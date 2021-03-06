# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20181025_1946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='building',
            name='stars',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='bookingdate',
            name='booking',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Booking'),
        ),
        migrations.AlterField(
            model_name='bookingdate',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
