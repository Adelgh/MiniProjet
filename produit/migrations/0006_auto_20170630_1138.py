# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-30 09:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import produit.models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0005_auto_20170629_0255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(default=None, upload_to=produit.models.group_based_upload_to_seconder)),
                ('image2', models.ImageField(default=None, upload_to=produit.models.group_based_upload_to_seconder)),
                ('image3', models.ImageField(default=None, upload_to=produit.models.group_based_upload_to_seconder)),
            ],
        ),
        migrations.RemoveField(
            model_name='produit',
            name='logo1',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='logo2',
        ),
        migrations.RemoveField(
            model_name='produit',
            name='logo3',
        ),
        migrations.AddField(
            model_name='produit',
            name='categorie',
            field=models.CharField(choices=[('bijoux', 'bijoux'), ('maison et ameublement', 'maison et ameublement'), ('vetements', 'vetements'), ('art et collections', 'art et collections'), ('accessoires', 'accessoires'), ('sacs et bagages', 'sacs et bagages'), ('mariage', 'mariage')], default='bijoux', max_length=250),
        ),
        migrations.AddField(
            model_name='produit',
            name='image',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='produit.Image'),
        ),
    ]