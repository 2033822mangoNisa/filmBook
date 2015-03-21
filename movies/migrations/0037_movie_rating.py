# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0036_auto_20150319_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=0.0),
            preserve_default=True,
        ),
    ]
