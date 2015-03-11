# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0025_auto_20150306_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
