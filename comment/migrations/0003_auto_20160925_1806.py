# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-25 15:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20160923_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(blank=True, max_length=140, verbose_name='Текст комментария'),
        ),
    ]