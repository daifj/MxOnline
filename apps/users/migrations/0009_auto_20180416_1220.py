# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20180415_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(default='', upload_to='banner/%Y/%m', verbose_name='轮播图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='image/%Y/%m', verbose_name='头像'),
        ),
    ]