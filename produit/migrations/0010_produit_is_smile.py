# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0009_produit_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='is_smile',
            field=models.BooleanField(default=False),
        ),
    ]
