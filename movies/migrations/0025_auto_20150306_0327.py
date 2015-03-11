# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0024_auto_20150303_2226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='type',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
    ]
