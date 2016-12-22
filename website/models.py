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

    # ANIMAL_TYPE_CHOICES = (
        # ('cat', 'Cats and Kittens'),
        # ('rabbit_gp', 'Rabbits and Guinea Pigs'),
        # ('small_furries', 'Small furries'),
        # ('other', 'Other'),
    # )

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

