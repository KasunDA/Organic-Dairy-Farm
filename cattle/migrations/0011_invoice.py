# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-15 13:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cattle', '0010_auto_20161115_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer_name', models.CharField(max_length=50)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Quantity', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('Rate', models.DecimalField(decimal_places=2, default=12.5, max_digits=5)),
                ('Dues', models.IntegerField(default=0)),
                ('Total_amt', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('Amount_given', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('New_Dues', models.IntegerField(default=0)),
                ('Payment_Date', models.DateField()),
            ],
        ),
    ]
