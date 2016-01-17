# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 04:44
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_auto_20160109_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='\u95ee\u9898')),
                ('solution', models.TextField(verbose_name='\u7b54\u6848')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '\u5b66\u5458\u5e38\u89c1\u95ee\u9898\u6c47\u603b',
                'verbose_name_plural': '\u5b66\u5458\u5e38\u89c1\u95ee\u9898\u6c47\u603b',
            },
        ),
        migrations.AlterField(
            model_name='compliant',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65e5\u671f'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='valid_end_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 9, 4, 44, 52, 500196, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='studentfaq',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u4f5c\u8005'),
        ),
    ]