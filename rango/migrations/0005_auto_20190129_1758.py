# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-29 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_auto_20190129_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
