from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Genre, Actor


def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.all()
    tdk = Genre.objects.filter(movie__title='The Dark Knight')
    context_dict = {'genres': genres, 'movies': movies, 'tdk': tdk}

    return render(request, 'movies/index.html', context_dict)


def genre(request, genre_name_slug):
    context_dict = {}

    try:
        genre = Genre.objects.get(slug=genre_name_slug)
        context_dict['genre_name'] = genre.name

        movies = Movie.objects.filter(genres=genre)


        context_dict['movies'] = movies
        context_dict['genre'] = genre
        context_dict['genre_name_slug'] = genre_name_slug


    except Genre.DoesNotExist:
        pass

    return render(request, 'movies/genre.html', context_dict)


def movie(request, movie_name_slug):
    context_dict = {}

    try:
        movie = Movie.objects.get(slug=movie_name_slug)
        genres = Genre.objects.filter(movie__title=movie)
        actors = Actor.objects.filter(movie__title=movie)
        context_dict['movie'] = movie
        context_dict['genres'] = genres
        context_dict['actors'] = actors

    except Movie.DoesNotExist:
        pass

    return render(request, 'movies/movie.html', context_dict)


def actor(request, actor_name_slug):
    context_dict = {}

    try:
        actor = Actor.objects.get(slug=actor_name_slug)
        movies = Movie.objects.filter(actors=actor)
        #movies = Actor.objects.filter(movie__title='The Dark Knight')
        context_dict['actor'] = actor
        context_dict['movies'] = movies

    except Actor.DoesNotExist:
        pass

    return render(request, 'movies/actor.html', context_dict)
