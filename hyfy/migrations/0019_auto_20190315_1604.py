# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-15 16:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0018_auto_20190315_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]
