# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=60)
    password = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)



class Child(models.Model):
    first_name = models.CharField(max_length=15)
    middle_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    birthdate  = models.DateField()
    parent = models.ManyToManyField(User, related_name="child")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
