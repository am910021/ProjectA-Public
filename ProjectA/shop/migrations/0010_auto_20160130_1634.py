# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 08:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_item_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='item',
            name='image2',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]