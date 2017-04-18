# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 06:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0011_auto_20170418_0626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='shopping_app.Product'),
        ),
    ]
