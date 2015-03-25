# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0051_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='movie',
            field=models.ForeignKey(to='movies.Movie', null=True),
            preserve_default=True,
        ),
    ]
