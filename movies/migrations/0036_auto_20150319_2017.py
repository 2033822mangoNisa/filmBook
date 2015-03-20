# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0035_auto_20150319_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=models.ImageField(default=b'movie_images/default_movie_picture.jpg', upload_to=b'movie_images'),
            preserve_default=True,
        ),
    ]
