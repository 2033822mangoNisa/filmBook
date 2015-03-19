# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0030_movie_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 16, 23, 29, 4, 98000, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='picture',
            field=models.ImageField(upload_to=b'movie_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
