# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0032_auto_20150317_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.ImageField(upload_to=b'movie_images', blank=True),
            preserve_default=True,
        ),
    ]
