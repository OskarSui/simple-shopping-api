# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-08 19:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20170608_0336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='checked_out',
        ),
    ]
