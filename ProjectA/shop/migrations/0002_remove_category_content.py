# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-11 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
    ]