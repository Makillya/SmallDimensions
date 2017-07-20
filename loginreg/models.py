# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=60)
    street = models.CharField(max_length=40)
    apt = models.CharField(max_length=6)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.IntegerField()
    status = models.CharField(max_length=7, default="pending")


class Child(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthdate  = models.DateField()
    parent = models.ManyToManyField(User, related_name="child")
