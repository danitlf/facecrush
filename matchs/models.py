# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Match(models.Model):
    user_one = models.CharField(max_length=1000)
    user_two = models.CharField(max_length=1000)
