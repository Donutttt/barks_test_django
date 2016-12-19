from __future__ import unicode_literals
from django.utils import timezone
from datetime import *


from django.db import models

class Animal (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    record_input = models.DateTimeField(default=timezone.now)
    age = models.FloatField(default=0)
