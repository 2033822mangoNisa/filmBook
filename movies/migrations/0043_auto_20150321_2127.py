# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0042_userprofile_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='watchlist',
            field=models.ManyToManyField(to='movies.Movie', null=True, blank=True),
            preserve_default=True,
        ),
    ]
