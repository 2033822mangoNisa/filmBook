# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0017_comment_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default='', to='movies.Movie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='movie',
            field=models.ForeignKey(default='', to='movies.Movie'),
            preserve_default=False,
        ),
    ]
