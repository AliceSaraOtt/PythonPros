# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 21:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0011_article_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cat', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='cat',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='app1.cat'),
            preserve_default=False,
        ),
    ]
