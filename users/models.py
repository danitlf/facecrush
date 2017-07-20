# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
	user_id = models.CharField(max_length=1000)
	nome = models.CharField(max_length=1000)
	token = models.CharField(max_length=1000)

class Meta: 
	ordering = ('created',)