# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20161222_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_detail',
            field=models.TextField(max_length=300),
        ),
    ]
