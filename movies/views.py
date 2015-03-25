from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import datetime
from movies.models import Movie, Genre, Actor, Character, MovieRating, UserProfile, Producer
from movies.forms import MovieForm, CharacterForm, CommentForm, UserProfileForm, Comment
import operator


def index(request):
    genres = Genre.objects.all().order_by('name')
    movies = Movie.objects.order_by('title')

    movies_ratings = Movie.objects.all().order_by('-rating')[:10]

    context_dict = {'genres': genres, 'movies': movies, 'top_movies': movies_ratings}

    return render(request, 'movies/index.html', context_dict)


def genres(request):

    # initialize dictionary with movies filtered based on genre
    movies_dict = {}
    genres = Genre.objects.all()
    for genre in genres:
        movies_dict[genre.name] = []

    # add movies to dictionary
    movies = Movie.objects.all()
    for movie in movies:
        for g in movie.genres.all():
            movies_dict[g.name].append(movie)

    context_dict = {'genres': genres, 'movies': movies_dict}

    return render(request, 'movies/genres.html', context_dict)


def actors(request):
    actors = Actor.objects.order_by('name')
    producers = Producer.objects.all().order_by('last_name')
    available_actors = Actor.objects.filter(available='yes')


    context_dict = {'actors': actors, 'producers': producers, 'available_actors': available_actors}

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
        ratings = movie.get_rating()
        rating = ratings['rating']
        ratings_no = ratings['ratings_no']

        # get the movie's comments
        comments = Comment.objects.filter(movie=movie).order_by('-date')[:5]
        user_rating = 0
        already_in = 0

        if request.user.is_authenticated():
            user_profile = UserProfile.objects.get(user=request.user)
            user_ratings = MovieRating.objects.filter(user=user_profile)

            existing_rating = None
            for r in user_ratings:
                if r.movie == movie:
                    existing_rating = r

            if existing_rating is not None:
                user_rating = existing_rating.rating

            # check if movie is in user's watchlist

            for m in user_profile.watchlist.all():
                if m.id == movie.id:
                    already_in = 1

        else:
            user_profile = ''

        # add everything to context dictionary
        context_dict['movie'] = movie
        context_dict['genres'] = genres
        context_dict['actors'] = actors
        context_dict['characters'] = characters
        context_dict['range_char'] = range(len(characters))
        context_dict['character_actor'] = character_actor
        context_dict['rating'] = rating
        context_dict['comments'] = comments
        context_dict['user_profile'] = user_profile
        context_dict['user_rating'] = user_rating
        context_dict['ratings_no'] = ratings_no
        context_dict['already_in'] = already_in


        if request.method == 'POST':
            form = CommentForm(request.POST)

            if form.is_valid():
                comment = form.save(commit=False)
                comment.movie = movie
                comment.date = datetime.datetime.now()
                comment.user = user_profile

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

    user_profile = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():

            producer = Producer.objects.get(user=user_profile)
            movie = movie_form.save(commit=False)
            movie.user = producer

            if 'picture' in request.FILES:
                movie.picture = request.FILES['picture']

            movie.save()

            return HttpResponseRedirect('/movies/' + movie.slug + '/add_character/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print movie_form.errors

    else:
        movie_form = MovieForm()

    return render(request, 'movies/add_movie.html', {'movie_form': movie_form, 'user_profile': user_profile})


def add_character(request, movie_slug):
    user_profile = UserProfile.objects.get(user=request.user)

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
                                                         'character_actor': character_actor,
                                                         'user_profile': user_profile})


def add_actor(request, movie_slug):
    movie = Movie.objects.get(slug=movie_slug)
    characters = Character.objects.filter(movie__title=movie.title)
    actors = movie.get_actors()
    user_profile = UserProfile.objects.get(user=request.user)

    # build a dictionary of form 'character':'actor'
    character_actor = {}
    for i in range(len(characters)):
        if i < len(actors):
            character_actor[characters[i]] = actors[i]
        else:
            character_actor[characters[i]] = ''

    all_actors = Actor.objects.all()
    actor_options = {}
    for a in all_actors:
        actor_options[a.id] = a.name + ' ' + a.last_name

    return render(request, 'movies/add_actor.html', {'character_actor': character_actor, 'actor_options': actor_options,
                                                     'movie': movie, 'user_profile': user_profile})


def assign_actor(request):
    character_id = None
    actor_id = None
    actor = None
    movie = None

    if request.method == 'GET':
        character_id = int(request.GET['c_id'])
        actor_id = int(request.GET['a_id'])
        movie_id = int(request.GET['m_id'])

        character = Character.objects.get(id=character_id)
        actor = Actor.objects.get(id=actor_id)
        movie = Movie.objects.get(id=movie_id)

        character.actor = actor
        character.save()

    return HttpResponse(actor.user.first_name)


def user_profile_registration(request, username):

    USER_TYPES = {1: 'Member', 2: 'Actor', 3: 'Producer'}

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user = User.objects.get(username=username)
            profile = form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            user_profile = UserProfile.objects.get(user=request.user)

            if int(user_profile.type) == 2:
                Actor.objects.get_or_create(user=user_profile, name=user_profile.first_name,
                                            last_name=user_profile.last_name, info=user_profile.info)
            elif int(user_profile.type) == 3:
                Producer.objects.get_or_create(user=user_profile, first_name=user_profile.first_name,
                                               last_name=user_profile.last_name, info=user_profile.info)

            return HttpResponseRedirect('/movies/')

        else:
            print form.errors

    else:

        form = UserProfileForm()

    return render(request, 'movies/user_profile_form.html', {'form': form, 'username': username, 'types': USER_TYPES})


def edit_profile(request, username):
    context_dict = {}
    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)

    if user_profile.type == '2':
        actor = Actor.objects.get(user=user_profile)
        movies_played_in = actor.get_movies()
        context_dict['movies_played_in'] = movies_played_in
    elif user_profile.type == '3':
        producer = Producer.objects.get(user=user_profile)
        movies_produced = producer.get_movies()
        context_dict['movies_produced'] = movies_produced

    watchlist = user_profile.watchlist.all()[:10]
    context_dict['watchlist'] = watchlist

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            else:
                profile.picture = user_profile.picture

            profile.save()

            return HttpResponseRedirect('/movies/user/' + username)

        else:
            print form.errors

    else:

        form = UserProfileForm()

    context_dict['form'] = form
    context_dict['username'] = username
    context_dict['user_profile'] = user_profile

    return render(request, 'movies/edit_profile.html', context_dict)


def search(request):
    query = None
    if request.method == 'POST':
        if 'search_textbox' in request.POST:
            query = request.POST['search_textbox']

    return render(request, 'movies/search.html', {'query': query})


@login_required
def profile(request, username):

    context_dict = {}
    current_user = User.objects.get(username=request.user.username)
    current_user_profile = UserProfile.objects.get(user=current_user)
    context_dict['current_user'] = current_user

    user = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=user)
    if user_profile.type == '1':
        context_dict['user_type'] = 'Member'
    elif user_profile.type == '2':
        context_dict['user_type'] = 'Actor'
        actor = Actor.objects.get(user=user_profile)
        movies_played_in = actor.get_movies()
        context_dict['movies_played_in'] = movies_played_in

    elif user_profile.type == '3':
        context_dict['user_type'] = 'Producer'
        producer = Producer.objects.get(user=user_profile)
        movies_produced = producer.get_movies()
        context_dict['movies_produced'] = movies_produced

    watchlist = current_user_profile.watchlist.all()[:10]
    context_dict['watchlist'] = watchlist

    my_ratings = MovieRating.objects.filter(user=user_profile)
    context_dict['my_ratings'] = my_ratings

    my_comments = Comment.objects.filter(user=user_profile).order_by('-date')[:5]
    context_dict['my_comments'] = my_comments

    context_dict['user_profile'] = user_profile
    context_dict['current_user_profile'] = current_user_profile

    print context_dict

    return render(request, 'movies/profile.html', context_dict)


@login_required
def rate(request):
    movie_id = None
    rating = None
    user_id = None

    if request.method == 'GET':
        movie_id = request.GET['m_id']
        rating = int(request.GET['r'])
        user_id = request.GET['u_id']

    movie = Movie.objects.get(id=int(movie_id))
    user = User.objects.get(id=int(user_id))
    user_profile = UserProfile.objects.get(user=user)

    user_ratings = MovieRating.objects.filter(user=user_profile)

    existing_rating = None
    for r in user_ratings:
        if r.movie == movie:
            existing_rating = r

    if existing_rating is not None:
        existing_rating.rating = rating
        existing_rating.save()
    else:
        movie_rating_new = MovieRating.objects.get_or_create(movie=movie, user=user_profile, rating=rating)[0]

    ratings = movie.get_rating()
    new_rating = ratings['rating']
    new_ratings_no = ratings['ratings_no']

    # update movie's rating field
    movie.rating = new_rating
    movie.save()

    response_dict = {'rating': new_rating, 'ratings_no': new_ratings_no}
    # response_json = json.dump(['data', response_dict])

    return HttpResponse(new_rating)


def add_to_watchlist(request):
    movie_id = None
    user_id = None

    if request.method == 'GET':
        movie_id = request.GET['m_id']
        user_id = request.GET['u_id']

    movie = Movie.objects.get(id=movie_id)
    user = User.objects.get(id=user_id)
    user_profile = UserProfile.objects.get(user=user)

    user_profile.watchlist.add(movie)
    user_profile.save()

    return HttpResponse('')


def edit_movie(request, movie_slug):
    user_profile = UserProfile.objects.get(user=request.user)
    movie = Movie.objects.get(slug=movie_slug)

    if request.method == 'POST':
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():

            producer = Producer.objects.get(user=user_profile)
            movie = movie_form.save(commit=False)
            movie.user = producer

            if 'picture' in request.FILES:
                movie.picture = request.FILES['picture']

            movie.save()

            return HttpResponseRedirect('/movies/' + movie.slug + '/add_character/')
        else:
            # The supplied form contained errors - just print them to the terminal.
            print movie_form.errors

    else:
        movie_form = MovieForm()

    return render(request, 'movies/edit_movie.html', {'movie_form': movie_form, 'user_profile': user_profile,
                                                      'movie': movie})