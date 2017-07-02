# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-28 12:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Boutique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('logo', models.FileField(upload_to='')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('descreption', models.CharField(max_length=250)),
                ('logo', models.FileField(max_length=250, upload_to='')),
                ('boutique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produit.Boutique')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]