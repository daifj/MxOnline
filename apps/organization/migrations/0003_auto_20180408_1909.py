# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-08 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180408_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='course_nums',
            field=models.IntegerField(default=0, verbose_name='课程数'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='students',
            field=models.IntegerField(default=0, verbose_name='学习人数'),
        ),
    ]
