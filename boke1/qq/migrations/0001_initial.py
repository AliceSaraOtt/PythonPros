# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 14:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QQGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('brife', models.TextField(default='\u7fa4\u4e3b\u5f88\u61d2', max_length=30)),
                ('maxMember', models.IntegerField(default=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('friends', models.ManyToManyField(related_name='_userprofile_friends_+', to='qq.UserProfile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='admin',
            field=models.ManyToManyField(related_name='GroupAdmin', to='qq.UserProfile'),
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='founder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Groups', to='qq.UserProfile'),
        ),
        migrations.AddField(
            model_name='qqgroup',
            name='members',
            field=models.ManyToManyField(related_name='GroupMembers', to='qq.UserProfile'),
        ),
    ]
