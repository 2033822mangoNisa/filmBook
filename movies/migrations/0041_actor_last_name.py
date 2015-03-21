# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0040_auto_20150321_0333'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='last_name',
            field=models.CharField(default=b'', max_length=128),
            preserve_default=True,
        ),
    ]
