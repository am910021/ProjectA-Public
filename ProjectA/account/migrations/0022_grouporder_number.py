# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20160203_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouporder',
            name='number',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
    ]
