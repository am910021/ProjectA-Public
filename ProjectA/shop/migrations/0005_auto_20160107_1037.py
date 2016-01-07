# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 02:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20160107_0900'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='category',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
