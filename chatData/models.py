from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
    username = models.CharField(max_length = 50)
    password = models.CharField(max_length = 50)
