# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-02-04 11:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('systemAnalyst', '0003_items_barcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
