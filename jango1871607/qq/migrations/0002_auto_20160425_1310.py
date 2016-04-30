# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-25 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='QQgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='friend',
            field=models.ManyToManyField(blank=True, related_name='_userprofile_friend_+', to='qq.UserProfile'),
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='member',
            field=models.ManyToManyField(related_name='members', to='qq.UserProfile'),
        ),
    ]
