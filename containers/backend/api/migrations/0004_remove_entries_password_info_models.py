# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-25 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_mv_entries_to_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='password',
        ),
        migrations.RemoveField(
            model_name='entry',
            name='user',
        ),
        migrations.DeleteModel(
            name='Entry',
        ),
        migrations.DeleteModel(
            name='PasswordInfo',
        ),
    ]
