# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-13 12:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=128)),
                ('content', models.TextField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.CharField(max_length=100)),
                ('image', models.CharField(blank=True, max_length=128)),
                ('isActive', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('cost', models.IntegerField()),
                ('inventory', models.IntegerField()),
                ('image', models.CharField(blank=True, max_length=128)),
                ('image2', models.CharField(blank=True, max_length=128)),
                ('intro', models.TextField(blank=True)),
                ('introduction', models.TextField(blank=True)),
                ('ingredient', models.TextField(blank=True)),
                ('manual', models.TextField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
                ('sp', models.BooleanField(default=False)),
                ('new', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Category')),
            ],
        ),
    ]
