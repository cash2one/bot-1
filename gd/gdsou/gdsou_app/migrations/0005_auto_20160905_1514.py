# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-05 15:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gdsou_app', '0004_auto_20160905_1502'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Race',
            new_name='Races',
        ),
    ]