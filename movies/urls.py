from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$', views.genre, name='genre'),
                       url(r'^movie/(?P<movie_name_slug>[\w\-]+)/$', views.movie, name='movie'),
                       url(r'^actor/(?P<actor_name_slug>[\w\-]+)/$', views.actor, name='actor'),
                       url(r'^genres/$', views.genres, name='genres'),
                       url(r'^actors/$', views.actors, name='actors'),
                       )
