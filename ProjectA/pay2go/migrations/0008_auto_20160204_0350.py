# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 19:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pay2go', '0007_notifyurldb_group'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomerUrlDB',
            new_name='CustomerDB',
        ),
        migrations.RenameModel(
            old_name='NotifyUrlDB',
            new_name='NotifyDB',
        ),
    ]
