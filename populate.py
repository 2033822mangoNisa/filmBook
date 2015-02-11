import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

from movies.models import Genre, Movie


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

    # Add movies
    add_movie(
        genres=[drama, action, crime],
        title='The Dark Knight',
        year=2008
    )

    add_movie(
        genres=[drama, biography, thriller],
        title='The Imitation Game',
        year=2014
    )

    add_movie(
        genres=[drama],
        title='Boyhood',
        year=2014
    )

    add_movie(
        genres=[action, mystery, sci_fi],
        title='Inception',
        year=2010
    )

    add_movie(
        genres=[drama, romance, biography],
        title='The Theory of Everything',
        year=2014
    )

    add_movie(
        genres=[mystery, thriller],
        title='Memento',
        year=2000
    )

    add_movie(
        genres=[drama],
        title='Fight Club',
        year=1999
    )

    add_movie(
        genres=[comedy],
        title='Hot Fuzz',
        year=2007
    )

    for g in Genre.objects.all():
        for m in Movie.objects.filter(genres=g):
            print "- {0} - {1}".format(str(g), str(m))


def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    return g


def add_movie(genres, title, year, producer='', writer=''):
    m = Movie.objects.get_or_create(title=title, year=year, producer=producer, writer=writer)[0]
    for genre in genres:
        m.genres.add(genre)
    return m

# Start execution here!
if __name__ == '__main__':
    print "Starting Movies population script..."
    populate()