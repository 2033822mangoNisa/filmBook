from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect
import datetime
from movies.models import Movie, Genre, Actor, Character, MovieRating, UserProfile
from movies.forms import MovieForm, CharacterForm, CommentForm, UserProfileForm, Comment


def index(request):
    genres = Genre.objects.all()
    movies = Movie.objects.order_by('title')



    context_dict = {'genres': genres, 'movies': movies}

    return render(request, 'movies/index.html', context_dict)


def genres(request):
    genres = Genre.objects.all()

    context_dict = {'genres': genres}

    return render(request, 'movies/genres.html', context_dict)


def actors(request):
    actors = Actor.objects.order_by('name')

    context_dict = {'actors': actors}

    return render(request, 'movies/actors.html', context_dict)


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
        genres = movie.genres.all()

        # get the movie's characters
        characters = movie.characters.all()

        # get the actors who play the characters
        actors = movie.get_actors()

        # build a dictionary of form 'character':'actor'
        character_actor = {}
        for i in range(len(actors)):
            character_actor[characters[i]] = actors[i]

        # get the movie's rating
        rating = movie.get_rating()

        # get the movie's comments
        comments = Comment.objects.filter(movie=movie).order_by('-date')

        # add everything to context dictionary
        context_dict['movie'] = movie
        context_dict['genres'] = genres
        context_dict['actors'] = actors
        context_dict['characters'] = characters
        context_dict['range_char'] = range(len(characters))
        context_dict['character_actor'] = character_actor
        context_dict['rating'] = rating
        context_dict['comments'] = comments

        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.movie = movie
                comment.date = datetime.datetime.now()
                comment.user = request.user

                comment.save()
                return HttpResponseRedirect('/movies/movie/' + movie_name_slug)
            else:

                print form.errors

        else:
            form = CommentForm()

        context_dict['comment_form'] = form

    except Movie.DoesNotExist:
        pass

    return render(request, 'movies/movie.html', context_dict)


def actor(request, actor_name_slug):
    context_dict = {}

    try:
        actor = Actor.objects.get(slug=actor_name_slug)
        characters = actor.get_characters()
        movies = actor.get_movies()
        rating = actor.get_rating()

        context_dict['actor'] = actor
        context_dict['movies'] = movies
        context_dict['rating'] = rating
        context_dict['characters'] = characters

    except Actor.DoesNotExist:
        pass

    return render(request, 'movies/actor.html', context_dict)


def add_movie(request):

    # A HTTP POST?
    if request.method == 'POST':
        movie_form = MovieForm(request.POST)

        # Have we been provided with a valid form?
        if movie_form.is_valid():
            # Save the new category to the database.
            movie = movie_form.save(commit=True)

            return HttpResponseRedirect('/movies/' + movie.slug + '/add_character/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print movie_form.errors

    else:
        # If the request was not a POST, display the form to enter details.
        movie_form = MovieForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'movies/add_movie.html', {'movie_form': movie_form})


def add_character(request, movie_slug):

    movie = Movie.objects.get(slug=movie_slug)
    characters = Character.objects.filter(movie__title=movie.title)
    actors = movie.get_actors()

    # build a dictionary of form 'character':'actor'
    character_actor = {}
    for i in range(len(characters)):
        if i < len(actors):
            character_actor[characters[i]] = actors[i]
        else:
            character_actor[characters[i]] = ''

    if request.method == 'POST':
        form = CharacterForm(request.POST)

        if form.is_valid():
            character = form.save(commit=True)
            movie.characters.add(character)

            return HttpResponseRedirect('/movies/' + movie.slug + '/add_character/')

        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors

    else:
        form = CharacterForm()

    return render(request, 'movies/add_character.html', {'form': form, 'movie': movie, 'characters': characters,
                                                         'character_actor': character_actor})


def user_profile_registration(request, username):

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():

            user = User.objects.get(username=username)
            profile = form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            return HttpResponseRedirect('/movies/')

        else:
            print form.errors

    else:

        form = UserProfileForm()

    return render(request, 'movies/user_profile_form.html', {'form': form, 'username': username})


def search(request):
    query = None
    if request.method == 'POST':
        if 'search_textbox' in request.POST:
            query = request.POST['search_textbox']

    return render(request, 'movies/search.html', {'query': query})


@login_required
def profile(request, username):
    context_dict = {}
    current_user = User.objects.get(username=username)
    context_dict['current_user'] = current_user
    #context_dict['user_type'] = None

    try:
        user_profile = UserProfile.objects.get(user=current_user)
        if user_profile.type == '1':
            context_dict['user_type'] = 'Member'
        elif user_profile.type == '2':
            context_dict['user_type'] = 'Actor'
        elif user_profile.type == '3':
            context_dict['user_type'] = 'Producer'
    except:
        user_profile = None

    context_dict['user_profile'] = user_profile

    return render(request, 'movies/profile.html', context_dict)



