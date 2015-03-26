# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0053_auto_20150325_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actorrating',
            name='actor',
        ),
        migrations.RemoveField(
            model_name='actorrating',
            name='user',
        ),
        migrations.DeleteModel(
            name='ActorRating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='review',
            name='user',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
