# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-19 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0019_auto_20161119_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cattle',
            name='Delivery_calf',
            field=models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female'), (b'Fail', b'Miscarriage')], default=b'Male', max_length=4),
        ),
        migrations.AlterField(
            model_name='cattle',
            name='sex',
            field=models.CharField(choices=[(b'Male', b'Male'), (b'Female', b'Female')], default=b'U', max_length=1),
        ),
    ]
