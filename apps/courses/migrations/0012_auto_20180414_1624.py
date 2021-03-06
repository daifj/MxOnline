# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-14 16:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_lesson_learn_times'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerCourse',
            fields=[
            ],
            options={
                'verbose_name': '轮播课程',
                'verbose_name_plural': '轮播课程',
                'proxy': True,
                'indexes': [],
            },
            bases=('courses.course',),
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='courses/%Y/%m', verbose_name='封面图'),
        ),
    ]
