# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-30 15:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_remove_mycart_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grouporder',
            name='paymentMethod',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grouporder',
            name='paymentStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grouporder',
            name='recipientStatus',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grouporder',
            name='totalAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='grouporder',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]