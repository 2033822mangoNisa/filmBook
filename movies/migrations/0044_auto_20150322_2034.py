# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0043_auto_20150321_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(to='movies.Producer', null=True),
            preserve_default=True,
        ),
    ]
