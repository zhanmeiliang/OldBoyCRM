# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-17 07:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0008_auto_20160117_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 16, 7, 21, 16, 773422, tzinfo=utc)),
        ),
    ]