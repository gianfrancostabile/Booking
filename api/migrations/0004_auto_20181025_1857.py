# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 21:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20181025_1851'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BookingDates',
            new_name='BookingDate',
        ),
    ]
