# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-31 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0010_auto_20161231_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='animalcontact',
            name='animal_name',
            field=models.CharField(default='none provided', max_length=200),
        ),
    ]