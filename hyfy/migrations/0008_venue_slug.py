# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-11 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0007_spotauth'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
