# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-20 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20160311_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='flight',
            name='key',
            field=models.IntegerField(null=True, unique=True),
        ),
    ]
