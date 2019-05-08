# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-01 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('category', models.CharField(max_length=300)),
                ('price', models.CharField(max_length=9)),
                ('numberOfItems', models.CharField(default=0, max_length=9)),
                ('desc', models.CharField(max_length=500)),
                ('status', models.BooleanField()),
            ],
        ),
    ]
