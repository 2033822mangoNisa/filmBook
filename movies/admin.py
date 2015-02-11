from django.contrib import admin
from movies.models import Movie, Genre, Actor

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
