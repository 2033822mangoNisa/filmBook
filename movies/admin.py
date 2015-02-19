from django.contrib import admin
from movies.models import Movie, Genre, Actor, Character, UserProfile, MovieRating, ActorRating

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Character)
admin.site.register(UserProfile)
admin.site.register(MovieRating)
admin.site.register(ActorRating)


