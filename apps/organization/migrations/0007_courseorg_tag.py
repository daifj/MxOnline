# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-13 21:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_teacher_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='机构标签'),
        ),
    ]