# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-27 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MW', '0006_auto_20160624_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='pub_date',
            field=models.DateField(),
        ),
    ]
