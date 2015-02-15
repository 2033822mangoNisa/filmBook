from django.db import models
from django.template.defaultfilters import slugify


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=128)
    info = models.TextField(blank=True)
    link = models.URLField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Actor, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Character(models.Model):
    name = models.CharField(max_length=128)
    actor = models.ForeignKey(Actor)

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(default=0)
    producer = models.CharField(max_length=128, blank=True)
    writer = models.CharField(max_length=128, blank=True)
    genres = models.ManyToManyField(Genre)
    characters = models.ManyToManyField(Character)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title










