# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-27 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cattle',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
    ]
