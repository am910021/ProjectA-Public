# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-04 17:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_delete_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='price',
            new_name='cost',
        ),
    ]
