# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 10:38
from __future__ import unicode_literals

import companylist.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('companylist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='content',
            field=models.TextField(default=datetime.datetime(2016, 2, 28, 10, 38, 32, 659632, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=companylist.models.upload_location, width_field='width_field'),
        ),
        migrations.AddField(
            model_name='company',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
    ]
