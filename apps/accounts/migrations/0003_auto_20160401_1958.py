# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-02 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_emailuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailuser',
            name='username',
            field=models.CharField(max_length=24),
        ),
    ]