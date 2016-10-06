# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-17 21:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=30, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=30, verbose_name='Фамилия')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(verbose_name='Дата смерти')),
                ('biography', models.TextField(blank=True, verbose_name='Биография')),
                ('photo', models.ImageField(blank=True, upload_to='authors/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.CreateModel(
            name='Verse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('year_of_writing', models.CharField(blank=True, max_length=200, validators=[django.core.validators.RegexValidator(code='Invalid year', message='You must enter a year', regex='^\\d{4}$')], verbose_name='Год написания')),
                ('slug', models.SlugField(unique=True, verbose_name='Идентификатор')),
                ('text', models.TextField(blank=True, verbose_name='Текст произведения')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verses', to='verse.Author', verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Произведение',
                'verbose_name_plural': 'Произведения',
            },
        ),
    ]