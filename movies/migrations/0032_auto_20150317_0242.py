# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0031_auto_20150316_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'movie_images', blank=True),
            preserve_default=True,
        ),
    ]
