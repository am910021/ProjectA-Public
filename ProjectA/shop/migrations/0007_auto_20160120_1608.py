# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 08:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20160120_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Introduction',
            new_name='introduction',
        ),
    ]