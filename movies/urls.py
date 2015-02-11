from django.conf.urls import patterns, url
from movies import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^genre/(?P<genre_name_slug>[\w\-]+)/$', views.genre, name='genre'),
                       url(r'^movie/(?P<movie_name_slug>[\w\-]+)/$', views.movie, name='movie'),
                       )
