# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_auto_20170801_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderjob',
            name='paper_cost',
            field=models.IntegerField(default=0),
        ),
    ]