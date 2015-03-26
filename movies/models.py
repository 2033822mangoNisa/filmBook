from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)
    picture = models.ImageField(upload_to='profile_images', default='profile_images/default_user_picture.jpg')
    info = models.TextField(blank=True)
    type = models.CharField(max_length=128)
    watchlist = models.ManyToManyField('Movie', null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        try:
            existing = UserProfile.objects.get(user=self.user)
            self.type = existing.type
            self.id = existing.id
        except UserProfile.DoesNotExist:
            pass
        super(UserProfile, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Genre, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Actor(models.Model):
    user = models.OneToOneField(UserProfile, null=True)
    name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128, default='')
    info = models.TextField(blank=True)
    link = models.URLField(blank=True)
    available = models.CharField(max_length=3, default='no')

    def get_characters(self):
        return Character.objects.filter(actor__name=self.name)

    def get_movies(self):
        characters = self.get_characters()
        return Movie.objects.filter(characters=characters)

    def __unicode__(self):
        return self.name


class Producer(models.Model):
    user = models.OneToOneField(UserProfile, null=True)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    info = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def get_movies(self):
        return Movie.objects.filter(user=self)

    def save(self, *args, **kwargs):
        self.first_name = self.user.first_name
        self.last_name = self.user.last_name
        self.info = self.user.info
        super(Producer, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.user.user.username


class Character(models.Model):
    name = models.CharField(max_length=128)
    desc = models.TextField()
    actor = models.ForeignKey(Actor, blank=True, null=True)

    @staticmethod
    def get_character_list():
        characters = []
        i = 1
        for character in Character.objects.all():
            characters += (i, character.name)
            i += 1
        return characters

    def __unicode__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=128)
    year = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre)
    characters = models.ManyToManyField(Character, blank=True)
    user = models.ForeignKey(Producer, null=True)
    picture = models.ImageField(upload_to='movie_images', default='movie_images/default_movie_picture.jpg')
    summary = models.TextField()
    date_added = models.DateTimeField()
    link = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    slug = models.SlugField(unique=True, blank=True)

    def get_rating(self):
        ratings_list = {}
        ratings = MovieRating.objects.filter(movie=self)

        ratings_sum = 0
        ratings_no = 0
        for r in ratings:
            ratings_sum += r.rating
            ratings_no += 1

        if len(ratings) != 0:
            rating = ratings_sum/len(ratings)
        else:
            rating = 0

        ratings_list['rating'] = rating
        ratings_list['ratings_no'] = ratings_no

        return ratings_list

    def show_rating(self):
        return self.get_rating()['rating']

    def get_image(self):
        if self.picture:
            return self.picture.url
        else:
            return 'movie_images/default_movie_picture.jpg'

    def get_actors(self):
        actors = []
        for character in self.characters.all():
            actors += Actor.objects.filter(character__name=character)

        return actors

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.date_added = datetime.now()
        super(Movie, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title


class MovieRating(models.Model):
    movie = models.ForeignKey(Movie)
    user = models.ForeignKey(UserProfile)
    rating = models.FloatField()

    def __unicode__(self):
        return self.movie.title


class Notification(models.Model):
    sender = models.ForeignKey(Actor)
    receiver = models.ForeignKey(Producer)
    message = models.TextField()
    date = models.DateTimeField()
    movie = models.ForeignKey(Movie)

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        super(Notification, self).save(*args, **kwargs)


class Comment(models.Model):
    comment = models.CharField(max_length=256)
    date = models.DateTimeField(null=True)
    user = models.ForeignKey(UserProfile)
    movie = models.ForeignKey(Movie)











