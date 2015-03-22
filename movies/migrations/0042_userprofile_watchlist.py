# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0041_actor_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='watchlist',
            field=models.ManyToManyField(to='movies.Movie', null=True),
            preserve_default=True,
        ),
    ]
