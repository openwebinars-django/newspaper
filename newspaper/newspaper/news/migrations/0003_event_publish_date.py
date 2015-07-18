# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='publish_date',
            field=models.DateTimeField(default='2015-07-15 19:45', verbose_name='publish date'),
            preserve_default=False,
        ),
    ]
