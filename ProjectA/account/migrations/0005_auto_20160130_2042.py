# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20160130_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycart',
            name='date',
            field=models.DateField(),
        ),
    ]