from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


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

    def get_rating(self):
        ratings = ActorRating.objects.filter(actor=self)

        ratings_sum = 0
        for r in ratings:
            ratings_sum += r.rating

        if len(ratings) != 0:
            rating = ratings_sum/len(ratings)
        else:
            rating = 0

        return rating

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

    def get_rating(self):
        ratings = MovieRating.objects.filter(movie=self)

        ratings_sum = 0
        for r in ratings:
            ratings_sum += r.rating

        if len(ratings) != 0:
            rating = ratings_sum/len(ratings)
        else:
            rating = 0

        return rating

    def get_actors(self):
        actors = []
        for character in self.characters.all():
            actors += Actor.objects.filter(character__name=character)

        return actors


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=128)

    def __unicode__(self):
        return self.user.username


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(UserProfile)
    rating = models.FloatField()

    def __unicode__(self):
        return self.movie.title


class ActorRating(models.Model):
    actor = models.ForeignKey(Actor)
    user = models.ForeignKey(UserProfile)
    rating = models.FloatField()

    def __unicode__(self):
        return self.actor.name










