# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20170803_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]