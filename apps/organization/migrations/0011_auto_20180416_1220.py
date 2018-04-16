# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0010_auto_20180415_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='image',
            field=models.ImageField(default='', upload_to='org/%Y/%m', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(default='', upload_to='teacher/%Y/%m', verbose_name='头像'),
        ),
    ]
