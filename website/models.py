from __future__ import unicode_literals
from django.utils import timezone
from datetime import *


from django.db import models

class Animal(models.Model):

    ANIMAL_TYPES = [
        'Cats and Kittens',
        'Rabbits and Guinea Pigs',
        'Small Furries',
        'Other',
    ]

    ANIMAL_TYPE_CHOICES = [(_animal_type, _animal_type) for _animal_type in ANIMAL_TYPES]

    name = models.CharField(max_length=200)
    description = models.TextField()
    record_input = models.DateTimeField(default=timezone.now)
    age = models.FloatField(default=0)
    type = models.CharField(
                max_length=50,
                choices = ANIMAL_TYPE_CHOICES,
                default = 'other',
            )
    image = models.ImageField()

    def __unicode__(self):
        return self.name



class NewsItem(models.Model):

    title = models.CharField(max_length=200)
    body = models.TextField()
    record_input = models.DateTimeField(default=timezone.now)
    image = models.ImageField()

    def __unicode__(self):
        return self.title


class Event(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    event_start = models.DateTimeField() 
    image = models.ImageField()

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    
    contact_name = models.CharField(max_length=200)
    contact_detail = models.CharField(max_length=300) 

    def __unicode__(self):
        return self.contact_name

