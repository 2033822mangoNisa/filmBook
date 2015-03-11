# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0018_auto_20150221_1950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(to='movies.Character', blank=True),
            preserve_default=True,
        ),
    ]
