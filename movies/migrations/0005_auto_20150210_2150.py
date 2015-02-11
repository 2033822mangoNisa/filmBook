# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20150210_2126'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Genre',
        ),
        migrations.RemoveField(
            model_name='moviecategory',
            name='category',
        ),
        migrations.RemoveField(
            model_name='moviecategory',
            name='movie',
        ),
        migrations.DeleteModel(
            name='MovieCategory',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='category',
            new_name='genre',
        ),
    ]
