# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0050_remove_movie_producer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message', models.TextField()),
                ('date', models.DateTimeField()),
                ('receiver', models.ForeignKey(to='movies.Producer')),
                ('sender', models.ForeignKey(to='movies.Actor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
