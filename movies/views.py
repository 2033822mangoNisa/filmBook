from django.shortcuts import render
from django.http import HttpResponse
from movies.models import Movie, Genre, Actor, Character


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

        # get the movie's genres
        genres = Genre.objects.filter(movie__title=movie)

        # get the movie's characters
        characters = Character.objects.filter(movie__title=movie)

        # get the actors who play the characters
        actors = []
        for character in characters:
            actors += Actor.objects.filter(character__name=character)

        character_actor = {}

        for i in range(len(characters)):
            character_actor[characters[i]] = actors[i]

        context_dict['movie'] = movie
        context_dict['genres'] = genres
        context_dict['actors'] = actors
        context_dict['characters'] = characters
        context_dict['range_char'] = range(len(characters))
        context_dict['character_actor'] = character_actor

    except Movie.DoesNotExist:
        pass

    return render(request, 'movies/movie.html', context_dict)


def actor(request, actor_name_slug):
    context_dict = {}

    try:
        actor = Actor.objects.get(slug=actor_name_slug)
        characters = Character.objects.filter(actor__name=actor)
        movies = Movie.objects.filter(characters=characters)
        #movies = Actor.objects.filter(movie__title='The Dark Knight')

        context_dict['actor'] = actor
        context_dict['movies'] = movies


    except Actor.DoesNotExist:
        pass

    return render(request, 'movies/actor.html', context_dict)
