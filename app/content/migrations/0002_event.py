# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-21 18:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, default=None, help_text='Full HTML allowed. Keep headers at h2 or smaller.', null=True)),
                ('address1', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('address2', models.CharField(blank=True, default=None, max_length=50, null=True)),
                ('city', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('datetime', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('cost', models.FloatField(default=0.0)),
                ('picture', models.TextField(blank=True, db_column='data', default=None, null=True)),
            ],
        ),
    ]
