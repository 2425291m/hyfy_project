# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0005_auto_20190310_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='slug',
            field=models.SlugField(),
        ),
    ]
