# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
            ],
            options={
                'verbose_name': 'event',
                'verbose_name_plural': 'events',
            },
        ),
    ]
