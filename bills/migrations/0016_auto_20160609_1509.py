# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 15:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0015_bills_billingmonth2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bills',
            name='billingMonth2',
            field=models.DateTimeField(blank=True, default=datetime.date(2016,2,4), null=True),
        ),
    ]
