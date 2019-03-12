# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0002_auto_20190310_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city_venue_set', to='hyfy.City'),
        ),
    ]