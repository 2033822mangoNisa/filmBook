# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0037_movie_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='user',
            field=models.OneToOneField(null=True, to='movies.UserProfile'),
            preserve_default=True,
        ),
    ]
