# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0019_auto_20150302_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='desc',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
