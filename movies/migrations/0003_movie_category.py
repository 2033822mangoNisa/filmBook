# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_moviecategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='category',
            field=models.ManyToManyField(to='movies.Category'),
            preserve_default=True,
        ),
    ]
