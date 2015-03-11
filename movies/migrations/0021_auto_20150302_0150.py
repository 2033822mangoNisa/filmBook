# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0020_character_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='actor',
            field=models.ForeignKey(to='movies.Actor', blank=True),
            preserve_default=True,
        ),
    ]
