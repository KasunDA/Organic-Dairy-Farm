# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0012_auto_20161115_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='Quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
