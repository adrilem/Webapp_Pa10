# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-28 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Usager',
        ),
    ]
