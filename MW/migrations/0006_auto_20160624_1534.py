# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-24 14:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MW', '0005_auto_20160624_1533'),
    ]

    operations = [
        migrations.RenameField(
            model_name='value',
            old_name='pubDate',
            new_name='pub_date',
        ),
    ]