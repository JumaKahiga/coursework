# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-01 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_orderjob_paper_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderjob',
            name='paper_cost',
        ),
    ]
