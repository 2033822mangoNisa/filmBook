# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0048_auto_20150324_2230'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='writer',
        ),
    ]
