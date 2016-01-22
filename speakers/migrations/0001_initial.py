# -*- coding: utf-8 -*-
# Generated by Django 1.9b1 on 2016-01-22 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField()),
                ('picture', models.ImageField(upload_to='')),
                ('twitter', models.CharField(blank=True, max_length=50)),
                ('github', models.CharField(blank=True, max_length=50)),
                ('talk_title', models.CharField(max_length=200)),
                ('talk_description', models.TextField()),
                ('confirmed', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
    ]