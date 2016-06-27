# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-24 11:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_A', models.FloatField()),
                ('value_B', models.FloatField()),
                ('pub_date', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]