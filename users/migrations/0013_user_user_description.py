# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 01:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_remove_user_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_description',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]
