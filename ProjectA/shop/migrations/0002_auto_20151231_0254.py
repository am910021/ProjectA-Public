# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(max_length=20),
        ),
    ]
