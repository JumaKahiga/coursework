# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_remove_orderjob_paper_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderjob',
            name='paper_cost',
            field=models.IntegerField(default=0),
        ),
    ]
