# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20160131_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='resetCode',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='fullName',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
