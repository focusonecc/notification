# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-05 13:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0003_auto_20171205_2100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'verbose_name': 'Notification', 'verbose_name_plural': 'Notification'},
        ),
    ]
