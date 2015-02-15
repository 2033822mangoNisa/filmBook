# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_auto_20150214_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='characters',
            field=models.ManyToManyField(to='movies.Character'),
            preserve_default=True,
        ),
    ]
