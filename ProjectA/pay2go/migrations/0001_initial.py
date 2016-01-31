# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 04:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerUrlDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(blank=True, max_length=128)),
                ('Message', models.CharField(blank=True, max_length=128)),
                ('MerchantID', models.CharField(blank=True, max_length=128)),
                ('Amt', models.CharField(blank=True, max_length=128)),
                ('TradeNo', models.CharField(blank=True, max_length=128)),
                ('MerchantOrderNo', models.CharField(blank=True, max_length=128)),
                ('PaymentType', models.CharField(blank=True, max_length=128)),
                ('CheckCode', models.CharField(blank=True, max_length=128)),
                ('ExpireDate', models.CharField(blank=True, max_length=128)),
                ('BankCode', models.CharField(blank=True, max_length=128)),
                ('CodeNo', models.CharField(blank=True, max_length=128)),
                ('Barcode_1', models.CharField(blank=True, max_length=128)),
                ('Barcode_2', models.CharField(blank=True, max_length=128)),
                ('Barcode_3', models.CharField(blank=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NotifyUrlDB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Status', models.CharField(blank=True, max_length=128)),
                ('Message', models.CharField(blank=True, max_length=128)),
                ('MerchantID', models.CharField(blank=True, max_length=128)),
                ('Amt', models.CharField(blank=True, max_length=128)),
                ('TradeNo', models.CharField(blank=True, max_length=128)),
                ('MerchantOrderNo', models.CharField(blank=True, max_length=128)),
                ('PaymentType', models.CharField(blank=True, max_length=128)),
                ('RespondType', models.CharField(blank=True, max_length=128)),
                ('CheckCode', models.CharField(blank=True, max_length=128)),
                ('PayTime', models.CharField(blank=True, max_length=128)),
                ('IP', models.CharField(blank=True, max_length=128)),
                ('EscrowBank', models.CharField(blank=True, max_length=128)),
                ('TokenUseStatus', models.CharField(blank=True, max_length=128)),
                ('RespondCode', models.CharField(blank=True, max_length=128)),
                ('Auth', models.CharField(blank=True, max_length=128)),
                ('Card6No', models.CharField(blank=True, max_length=128)),
                ('Card4No', models.CharField(blank=True, max_length=128)),
                ('Inst', models.CharField(blank=True, max_length=128)),
                ('InstFirst', models.CharField(blank=True, max_length=128)),
                ('InstEach', models.CharField(blank=True, max_length=128)),
                ('ECI', models.CharField(blank=True, max_length=128)),
                ('PayBankCode', models.CharField(blank=True, max_length=128)),
                ('PayerAccount5Code', models.CharField(blank=True, max_length=128)),
                ('CodeNo', models.CharField(blank=True, max_length=128)),
                ('Barcode_1', models.CharField(blank=True, max_length=128)),
                ('Barcode_2', models.CharField(blank=True, max_length=128)),
                ('Barcode_3', models.CharField(blank=True, max_length=128)),
            ],
        ),
    ]
