# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-15 15:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0016_auto_20190314_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.date(2019, 3, 15)),
        ),
    ]
