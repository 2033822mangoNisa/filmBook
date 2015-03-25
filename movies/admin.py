from django.contrib import admin
from movies.models import Movie, Genre, Actor, Character, UserProfile, MovieRating, ActorRating, Review, Comment, \
    Producer, Notification

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Actor)
admin.site.register(Character)
admin.site.register(UserProfile)
admin.site.register(MovieRating)
admin.site.register(ActorRating)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Producer)
admin.site.register(Notification)

