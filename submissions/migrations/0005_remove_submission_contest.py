# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-27 04:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_auto_20170127_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submission',
            name='contest',
        ),
    ]
