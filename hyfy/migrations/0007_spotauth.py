# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-10 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hyfy', '0006_auto_20190310_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='spotAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=50)),
                ('access_token', models.CharField(max_length=256, null=True)),
                ('refresh_token', models.CharField(max_length=256, null=True)),
                ('integration_user_id', models.CharField(max_length=256, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
