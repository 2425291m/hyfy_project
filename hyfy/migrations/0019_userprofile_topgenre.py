# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hyfy', '0018_auto_20190318_1649'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='topGenre',
            field=models.CharField(default='placeholder', max_length=50),
        ),
    ]
