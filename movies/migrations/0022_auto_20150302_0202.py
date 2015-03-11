# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0021_auto_20150302_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='actor',
            field=models.ForeignKey(blank=True, to='movies.Actor', null=True),
            preserve_default=True,
        ),
    ]
