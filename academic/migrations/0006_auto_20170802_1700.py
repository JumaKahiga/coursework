# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-02 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0005_orderjob_paper_cost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderjob',
            name='order_num',
        ),
        migrations.RemoveField(
            model_name='orderjob',
            name='paper_cost',
        ),
    ]