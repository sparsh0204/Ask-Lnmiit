# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20170830_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=1000),
        ),
    ]