# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0039_auto_20150321_0325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('info', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
                ('user', models.OneToOneField(null=True, to='movies.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='info',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
    ]
