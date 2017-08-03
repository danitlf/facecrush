# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import date

class User(models.Model):

	user_id = models.CharField(max_length=1000)
	name = models.CharField(max_length=1000)
	access_token = models.CharField(max_length=1000)
	description = models.CharField(max_length=1000, default=None)
	age = models.DateField(default=date.today)
	gender = models.CharField(max_length=10, default=None)
	show_gender = models.CharField(max_length=10, default=None)
	min_age = models.IntegerField(default=18)
	max_age = models.IntegerField(default=40)
	vip = models.BooleanField(default=False)

class Meta:
	ordering = ('created',)
