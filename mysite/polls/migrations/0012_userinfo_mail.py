# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-02-05 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_remove_books_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='mail',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
    ]
