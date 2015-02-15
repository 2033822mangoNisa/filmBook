# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0011_auto_20150214_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='actor',
            field=models.ForeignKey(to='movies.Actor'),
            preserve_default=True,
        ),
    ]
