# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-01-08 14:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='total_votes',
            field=models.IntegerField(default=0),
        ),
    ]
