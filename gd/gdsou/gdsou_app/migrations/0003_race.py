# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 13:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gdsou_app', '0002_vipuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('release_date', models.DateField()),
                ('belong', models.CharField(max_length=50)),
                ('return_date', models.DateField()),
                ('velocity', models.FloatField()),
                ('distance', models.FloatField()),
                ('company', models.CharField(max_length=50)),
                ('foot_num', models.CharField(max_length=50)),
                ('shed_num', models.IntegerField()),
                ('race_name', models.CharField(max_length=100)),
            ],
        ),
    ]
