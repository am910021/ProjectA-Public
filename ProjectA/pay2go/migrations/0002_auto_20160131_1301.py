# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pay2go', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerurldb',
            name='Amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='CheckCode',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='ExpireDate',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='MerchantID',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='MerchantOrderNo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='Message',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='PaymentType',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='Status',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='customerurldb',
            name='TradeNo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Amt',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Auth',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Barcode_1',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Barcode_2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Barcode_3',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Card4No',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Card6No',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='CheckCode',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='CodeNo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='ECI',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='EscrowBank',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='IP',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Inst',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='InstEach',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='InstFirst',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='MerchantID',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='MerchantOrderNo',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Message',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='PayBankCode',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='PayTime',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='PayerAccount5Code',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='PaymentType',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='RespondCode',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='RespondType',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='Status',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='TokenUseStatus',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='notifyurldb',
            name='TradeNo',
            field=models.CharField(max_length=20),
        ),
    ]
