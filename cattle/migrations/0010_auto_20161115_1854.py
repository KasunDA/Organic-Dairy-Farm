# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0009_auto_20161115_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='date_of_birth',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
