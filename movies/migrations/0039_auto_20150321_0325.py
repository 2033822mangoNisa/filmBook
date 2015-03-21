# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0038_actor_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='actor',
            name='available',
            field=models.CharField(default=b'no', max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(default=b'profile_images/default_user_picture.jpg', upload_to=b'profile_images'),
            preserve_default=True,
        ),
    ]
