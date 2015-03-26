# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0054_auto_20150326_0214'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField()),
                ('actor', models.ForeignKey(to='movies.Actor')),
                ('user', models.ForeignKey(to='movies.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
                ('user', models.ForeignKey(to='movies.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
