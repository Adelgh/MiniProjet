# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0012_auto_20170702_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='is_smile',
            field=models.BooleanField(default=False),
        ),
    ]
