# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_auto_20170124_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='problem',
            options={'ordering': ('id',), 'verbose_name': '问题', 'verbose_name_plural': '问题'},
        ),
    ]
