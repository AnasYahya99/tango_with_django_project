# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-29 17:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0008_auto_20190129_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='slug',
        ),
    ]
