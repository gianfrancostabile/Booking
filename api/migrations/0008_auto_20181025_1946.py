# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-25 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20181025_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdate',
            name='date',
            field=models.DateField(),
        ),
    ]
