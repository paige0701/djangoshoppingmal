# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-18 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0009_auto_20170417_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shopping_app.Comment'),
        ),
    ]
