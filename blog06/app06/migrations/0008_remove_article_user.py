# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app06', '0007_auto_20160316_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]
