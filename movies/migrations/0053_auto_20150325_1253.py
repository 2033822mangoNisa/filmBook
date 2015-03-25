# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0052_notification_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='movie',
            field=models.ForeignKey(default='', to='movies.Movie'),
            preserve_default=False,
        ),
    ]
