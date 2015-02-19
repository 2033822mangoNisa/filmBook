# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20150219_0125'),
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
            name='MovieRating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.FloatField()),
                ('movie', models.ForeignKey(to='movies.Movie')),
                ('user', models.ForeignKey(to='movies.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
