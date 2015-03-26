import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

from movies.models import UserProfile, Actor, Producer, Character, Genre, Movie
from django.contrib.auth.models import User


def add_movie(genres, characters, title, year, producer, summary=''):
    m = Movie.objects.get_or_create(title=title, year=year, user=producer, summary=summary)[0]

    print genres

    for genre in genres:
        m.genres.add(genre)

    print characters

    for character in characters:
        m.characters.add(character)

    return m


def add_char(name, actor):
    c = Character.objects.get_or_create(name=name, actor=actor)[0]

    return c


def add_genre(name):
    g = Genre.objects.get_or_create(name=name)[0]
    return g


def populate():
    # create users (a list of 20 users)
    # usernames: from test_user1 to test_user20
    # passwords: all the same - 'testpass'
    users = []
    for i in range(1, 21):
        new_user = User.objects.get_or_create(username="test_user"+str(i), email="emailaddres"+str(i)+"@adsas.com")[0]
        new_user.set_password("testpass")
        new_user.save()
        users.append(new_user)

    # create user profiles
    new_user_profile1 = UserProfile.objects.get_or_create(user=users[1], first_name="John", last_name='Adams',
                                                          info='First year digital media student.', type=3)[0]

    new_user_profile2 = UserProfile.objects.get_or_create(user=users[2], first_name="Sarah", last_name='Smith',
                                                          info='Youtuber and amatur film maker', type=3)[0]

    new_user_profile3 = UserProfile.objects.get_or_create(user=users[3], first_name="Jhene", last_name='Garrget',
                                                          info='Masters Student of  at Glasgow Calidonian', type=3)[0]

    new_user_profile4 = UserProfile.objects.get_or_create(user=users[4], first_name="Albert", last_name='McVitie',
                                                          info='Glasgow College of Arts Senior Lecturer', type=3)[0]

    new_user_profile5 = UserProfile.objects.get_or_create(user=users[5], first_name="Shona", last_name='Spencer',
                                                          info='I hope to start my degree in TV studies next year and become a producer', type=2)[0]

    new_user_profile6 = UserProfile.objects.get_or_create(user=users[6], first_name="Riffat", last_name='Nabi',
                                                          info='I am a big movie buff and enjoy watching indie movies', type=2)[0]

    new_user_profile7 = UserProfile.objects.get_or_create(user=users[7], first_name="Jamie", last_name='Smith',
                                                          info='Amature film maker and movie buff', type=1)[0]

    new_user_profile8 = UserProfile.objects.get_or_create(user=users[8], first_name="Emily", last_name='Elder',
                                                          info='I am an actress and also enjoy watching movies', type=2)[0]

    new_user_profile9 = UserProfile.objects.get_or_create(user=users[9], first_name="Helen", last_name='McDonald',
                                                          info='Glasgow College of Arts Senior Lecturer', type=1)[0]

    new_user_profile10 = UserProfile.objects.get_or_create(user=users[10], first_name="Amanda", last_name='Lee',
                                                           info='Movie Buff', type=1)[0]

    new_user_profile11 = UserProfile.objects.get_or_create(user=users[11], first_name="Li", last_name='Khan',
                                                           info='First year drama student. I would like to pursue acting', type=2)[0]

    new_user_profile12 = UserProfile.objects.get_or_create(user=users[12], first_name="Joe", last_name='Smith',
                                                           info='I make youtube review videos about new movies, I also leave in depth reviews about indie movies I see here', type=1)[0]

    new_user_profile13 = UserProfile.objects.get_or_create(user=users[13], first_name="Issac", last_name='Lamar',
                                                           info='I am a sound engineer working at Disney and also an asspiring actor.', type=2)[0]

    new_user_profile14 = UserProfile.objects.get_or_create(user=users[14], first_name="Humphrey", last_name='Clyde',
                                                           info='I want to be an actor', type=2)[0]

    new_user_profile15 = UserProfile.objects.get_or_create(user=users[15], first_name="Lola", last_name='Brook',
                                                           info='Studying media in high school and upload my course work onto this account', type=3)[0]

    new_user_profile16 = UserProfile.objects.get_or_create(user=users[16], first_name="Cristof", last_name='Remingon',
                                                           info='Amatur movie maker/producer/director', type=2)[0]

    new_user_profile17 = UserProfile.objects.get_or_create(user=users[17], first_name="Katie", last_name='Deeming',
                                                           info='Professional producer.', type=3)[0]

    new_user_profile18 = UserProfile.objects.get_or_create(user=users[18], first_name="Aleck", last_name='Bovick',
                                                           info='Media Student of  at University of Glasgow', type=2)[0]


    # create actors
    new_actor1 = Actor.objects.get_or_create(user=new_user_profile8, name=new_user_profile8.first_name,
                                             last_name=new_user_profile8.last_name,
                                             info='Filipino actress, active from 1999-2009.',
                                             link='http://en.wikipedia.org/wiki/Aleck_Bovick')[0]

    new_actor2 = Actor.objects.get_or_create(user=new_user_profile14, name=new_user_profile14.first_name,
                                             last_name=new_user_profile14.last_name,
                                             info='Samantha Barks is a 24 year old actress. Working on stage as well '
                                                  'as on screen',
                                             link='http://en.wikipedia.org/wiki/Samantha_Barks')[0]

    new_actor3 = Actor.objects.get_or_create(user=new_user_profile18, name=new_user_profile18.first_name,
                                             last_name=new_user_profile18.last_name,
                                             info='32 year old actor. Working mainly in english speaking roles as well '
                                                  'as some spanish roles.',
                                             link='a link, like the personal website of the actor or something like it')[0]

    new_actor4 = Actor.objects.get_or_create(user=new_user_profile16, name=new_user_profile16.first_name,
                                             last_name=new_user_profile16.last_name,
                                             info='With a honers degree in Drama from the Royal School of Arts in London '
                                                  'Humphrey has mainly worked on stage and is trying to break '
                                                  'onto the big sceen',
                                             link='')[0]

    new_actor5 = Actor.objects.get_or_create(user=new_user_profile5, name=new_user_profile5.first_name,
                                             last_name=new_user_profile5.last_name, info='18 year old actor. Working mainly '
                                                                                         'in english speaking roles as '
                                                                                         'well as some mongolian roles.',
                                             link='')[0]

    new_actor6 = Actor.objects.get_or_create(user=new_user_profile6, name=new_user_profile6.first_name,
                                             last_name=new_user_profile6.last_name,
                                             info='An up and coming actress, worked on a number of small movies as well '
                                                  'as staring on stage in the west end.',
                                             link='')[0]

    actors = [new_actor1, new_actor2, new_actor3, new_actor4, new_actor5, new_actor6]

    # create producers
    new_producer1 = Producer.objects.get_or_create(user=new_user_profile1, first_name=new_user_profile1.first_name,
                                                   last_name=new_user_profile1.last_name, info='',
                                                   link='')[0]

    new_producer2 = Producer.objects.get_or_create(user=new_user_profile2, first_name=new_user_profile2.first_name,
                                                   last_name=new_user_profile2.last_name, info='40 year old actor. With 20 years experiance John has worked on stage and on the big screen',
                                                   link='a link, like the personal website of the actor or something like it')[0]

    new_producer3 = Producer.objects.get_or_create(user=new_user_profile3, first_name=new_user_profile3.first_name,
                                                   last_name=new_user_profile3.last_name, info='Sarah is a young actress who currently stars in a BBC drama and has appeared in a number of short films',
                                                   link='')[0]

    new_producer4 = Producer.objects.get_or_create(user=new_user_profile4, first_name=new_user_profile4.first_name,
                                                   last_name=new_user_profile4.last_name, info='Worked many years in America, now a producer in Scotland',
                                                   link='http://www.deemingdreaming.com/')[0]

    new_producer5 = Producer.objects.get_or_create(user=new_user_profile17, first_name=new_user_profile5.first_name,
                                                   last_name=new_user_profile17.last_name, info='',
                                                   link='')[0]

    new_producer6 = Producer.objects.get_or_create(user=new_user_profile15, first_name=new_user_profile15.first_name,
                                                   last_name=new_user_profile15.last_name, info='Worked on many short films now pursueing at masters in TV Studies',
                                                   link='https://www.youtube.com/channel/UCV0vRq6CejTTOXsXaZjm9_w')

    # create characters ( a list of 20 characters)
    characters = []
    for i in range(1, 21):
        character = add_char('Character'+str(i), actors[i % 6])
        characters.append(character)

    # create genres
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

    # create movies
    movie1 = add_movie(
        characters=[characters[0], characters[1], characters[2]],    # this should be a list (of any length) of random characters from 'characters' list created above
        genres=[drama, action, crime],                               # a list of genres from the genres that were created
        title='Test Movie',
        year=2015,
        producer=new_producer1,                                      # one from the producers that were created
        summary="Summary example for a movie"                        # summary for movie (optional)
    )

    movie2 = add_movie(
        characters=[characters[5], characters[3], characters[15], characters[7]],
        genres=[adventure, fantasy],
        title='Another test movie',
        year=2014,
        producer=new_producer2,
        summary="Summary example for a movie"
    )

    # add more movies here




if __name__ == '__main__':
    print "Starting Movies population script..."
    populate()