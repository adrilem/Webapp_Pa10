# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 21:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20161128_2222'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(max_length=500)),
                ('password', models.CharField(max_length=100)),
                ('user_name', models.CharField(max_length=250)),
                ('user_logo', models.CharField(max_length=1000)),
            ],
        ),
    ]
