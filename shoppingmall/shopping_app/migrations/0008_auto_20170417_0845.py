# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-17 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0007_remove_product_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='photo/'),
        ),
    ]
