# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 14:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0015_auto_20161115_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calf',
            fields=[
                ('calf_Id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'NULL', max_length=30)),
                ('Breed', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(default=datetime.date.today, null=True)),
                ('age', models.IntegerField(default=0)),
                ('weight', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('sex', models.CharField(choices=[(b'M', b'Male'), (b'F', b'Female')], default=b'U', max_length=1)),
                ('pno_buyer', models.CharField(default=b'NULL', max_length=200)),
                ('pno_seller', models.CharField(default=b'NULL', max_length=200)),
                ('Insurance', models.BooleanField(choices=[(1, b'Yes'), (0, b'No')], default=0)),
                ('date_of_expiry_insurance', models.DateField(null=True)),
                ('dehorning', models.BooleanField(choices=[(1, b'Yes'), (0, b'No')], default=0)),
                ('One_time_Vaccination', models.BooleanField(choices=[(1, b'Yes'), (0, b'No')], default=0)),
                ('Remarks', models.CharField(default=b'NULL', max_length=200)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
