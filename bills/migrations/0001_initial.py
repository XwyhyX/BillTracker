# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-05 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=120)),
                ('billType', models.CharField(max_length=120)),
                ('amountDue', models.DecimalField(decimal_places=2, max_digits=19)),
                ('status', models.CharField(choices=[('PD', 'Paid'), ('UD', 'Unpaid')], default='UD', max_length=2)),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
                ('paymentDate', models.DateField()),
                ('inCharge', models.CharField(max_length=200)),
                ('proof', models.FileField(blank=True, null=True, upload_to=b'')),
            ],
            options={
                'ordering': ('-datePosted', '-status'),
            },
        ),
    ]
