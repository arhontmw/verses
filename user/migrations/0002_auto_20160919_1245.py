# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=1, null=True, verbose_name='Пол'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='isadmin',
            field=models.BooleanField(default=False, verbose_name='Права администратора'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, upload_to='users/%Y/%m/%d', verbose_name='Фотография'),
        ),
    ]
