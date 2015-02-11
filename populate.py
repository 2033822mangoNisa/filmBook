import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

from movies.models import Genre, Movie, Actor


def populate():

    # Add genre
    drama = add_genre('Drama')
    action = add_genre('Action')
    crime = add_genre('Crime')
    adventure = add_genre('Adventure')
    family = add_genre('Family')
    horror = add_genre('Horror')
    animation = add_genre('Animation')
    fantasy = add_genre('Fantasy')
    thriller = add_genre('Thriller')
    biography = add_genre('Biography')
    mystery = add_genre('Mystery')
    romance = add_genre('Romance')
    comedy = add_genre('Comedy')
    sci_fi = add_genre('Sci-Fi')

    # Add actors
    christian_bale = add_actor(name='Christian Bale')
    heath_ledger = add_actor(name='Heath Ledger')
    aaron_eckhart = add_actor(name='Aaron Eckhart')
    michael_caine = add_actor(name='Michael Caine')

    benedict_cumberbatch = add_actor(name='Benedict Cumberbatch')
    keira_knightley = add_actor(name='Keira Knightley')

    brad_pitt = add_actor(name='Brad Pitt')
    edward_norton = add_actor(name='Edward Norton')

    simon_pegg = add_actor(name='Simon Pegg')
    martin_freeman = add_actor(name='Martin Freeman')

    ellar_cotlane = add_actor(name='Ellar Cotlane')
    patricia_arquette = add_actor(name='Patricia Arquette')

    leonardo_dicaprio = add_actor(name='Leonardo DiCaprio')
    joseph_gordon_levitt = add_actor(name='Joseph Gordon-Levitt')

    guy_pearce = add_actor(name='Guy Pearce')

    eddie_redmayne = add_actor('Eddie Redmayne')
    felicity_jones = add_actor('Felicity Jones')


    # Add movies
    add_movie(
        actors=[christian_bale, heath_ledger, aaron_eckhart, michael_caine],
        genres=[drama, action, crime],
        title='The Dark Knight',
        year=2008
    )

    add_movie(
        actors=[benedict_cumberbatch, keira_knightley],
        genres=[drama, biography, thriller],
        title='The Imitation Game',
        year=2014
    )

    add_movie(
        actors=[ellar_cotlane, patricia_arquette],
        genres=[drama],
        title='Boyhood',
        year=2014
    )

    add_movie(
        actors=[leonardo_dicaprio, joseph_gordon_levitt],
        genres=[action, mystery, sci_fi],
        title='Inception',
        year=2010
    )

    add_movie(
        actors=[eddie_redmayne, felicity_jones],
        genres=[drama, romance, biography],
        title='The Theory of Everything',
        year=2014
    )

    add_movie(
        actors=[guy_pearce],
        genres=[mystery, thriller],
        title='Memento',
        year=2000
    )

    add_movie(
        actors=[brad_pitt, edward_norton],
        genres=[drama],
        title='Fight Club',
        year=1999
    )

    add_movie(
        actors=[simon_pegg, martin_freeman],
        genres=[comedy],
        title='Hot Fuzz',
        year=2007
    )

    add_movie(
        actors=[christian_bale, michael_caine],
        genres=[drama, thriller, mystery],
        title='The Prestige',
        year=2006
    )

    for g in Genre.objects.all():
        for m in Movie.objects.filter(genres=g):
            print "- {0} - {1}".format(str(g), str(m))
    for a in Actor.objects.all():
        print a


def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    return g


def add_movie(genres, actors, title, year, producer='', writer=''):
    m = Movie.objects.get_or_create(title=title, year=year, producer=producer, writer=writer)[0]

    for genre in genres:
        m.genres.add(genre)

    for actor in actors:
        m.actors.add(actor)

    return m


def add_actor(name, info='', link=''):
    a = Actor.objects.get_or_create(name=name, info=info, link=link)[0]
    return a

# Start execution here!
if __name__ == '__main__':
    print "Starting Movies population script..."
    populate()