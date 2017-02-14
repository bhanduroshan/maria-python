# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-02-14 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataplot', '0002_auto_20170214_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chartdata',
            options={'verbose_name': 'Data', 'verbose_name_plural': 'Data'},
        ),
        migrations.AddField(
            model_name='chartdata',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='chartdata',
            name='ticker',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
