# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-28 08:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/news/', verbose_name='Изображение новости'),
            preserve_default=False,
        ),
    ]
