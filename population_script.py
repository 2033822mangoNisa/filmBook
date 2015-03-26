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
    for i in range(1, 20):
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
                                             link='')[0]

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
                                                   link='https://www.youtube.com/channel/UCV0vRq6CejTTOXsXaZjm9_w')[0]

    # create characters ( a list of characters)
    characters = []
    for i in range(1, 7):
        character = add_char('Character'+str(i), actors[i-1])
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
        genres=[drama, action, family],                               # a list of genres from the genres that were created
        title='A Tale of Two Kitties',
        year=2015,
        producer=new_producer1,                                      # one from the producers that were created
        summary='This story will truly pull at your heart strings. It is a tale of a curious kitty called Magma wanting to' 
                ' make it big in the cat world, leave this life behind the impoverished life she was born into. On her journey'
                ' she meets a handsome but equally curious kitty called Milo who is on a journey of his own, to leave behind'
                ' is life of luxury and fame and live a simple family life. Can these two help each other out?'
                ' Or will curiosity kill these kitties.'              # summary for movie (optional)
    )

    movie2 = add_movie(
        characters=[characters[0], characters[4], characters[5], characters[3]],
        genres=[romance, thriller],
        title='The End of the Beginning',
        year=2013,
        producer=new_producer2,
        summary= ''
                 'No one could anticipate that the end was coming, the end of the beginning.'
                 ' When it arrives, it hits hard!' 
                 ' Lives are in tatters.'
                 ' Minds are boggled.'
                 ' First dates end FOREVER.'
                 ' Which wont be hard on anyone, after all it was only the end of the BEGINNING!'
    )

    movie3 = add_movie(
        characters=[characters[5], characters[1], characters[2], characters[3]],
        genres=[romance, thriller],
        title='The Beginning of The End',
        year=2014,
        producer=new_producer2,
        summary='The sequal to the end of the beginning'
                ' Its what you have been waiting for. The Beginning of The End.'
                ' Will Billy help the world to fly to a new planet to start over?'
                ' There are only 8 minutes to decide the fate of the world, will Sally make another appearance?'
                ' Will Sally take no for an answer or will she ruin everything for Billy, did she not understand when Billy'
                ' Jumped out the window on their first date it was the End of the Beginning?' 
    )

    movie4 = add_movie(
        characters=[characters[4], characters[5]],
        genres=[romance, horror, thriller],
        title='The Beginning',
        year=2016,
        producer=new_producer2,
        summary= 'Prequel of: The end of the Beginning'
                 ' You wanted to to know what happening in the beginning before it ended?'
                 ' Well now is your chance, in this romantic horror which will have you glues to your seats'
                 ' Why did Billy Joe Bob leave out the window on his first date with Shelly? Now we find out'
    )

    movie5 = add_movie(
        characters=[characters[1], characters[2], characters[3], characters[4], characters[5], characters[0]],
        genres=[fantasy, romance, horror],
        title='The Frog who wanted to be a Toad',
        year=2012,
        producer=new_producer3,
        summary='Flogaloid always wanted to be a Toad, ever since he fell'
                ' in love with toad next door, but he knows it can never be'
                ' she is only into toads.'
                ' So he diguises himself as a toad to win her heart'
                ' What happens when he finds out she was infact a homeless turtle? Will their love last?'
    )

    movie6 = add_movie(
        characters=[characters[0], characters[1]],
        genres=[adventure, comedy],
        title='Learning Greed',
        year=2014,
        producer=new_producer4,
        summary='Can greed be learnt? Jim Bob sure hopes so, he is the least greedy man in the world'
                ' and it is costing him fortune! He goes to the USA to find the greediest man in the world'
                ' and learn his ways.'
    )

    movie7 = add_movie(
        characters=[characters[5], characters[3], characters[5], characters[0]],
        genres=[adventure, fantasy, crime, sci_fi],
        title='Im out robbing',
        year=2014,
        producer=new_producer5,
        summary='Her son is a good for nothing intergalactic robber'
                ' She is the Queen of the world'
                ' How will she and can she pass on the crown to him?'
                ' Can she teach him to be on the straight and narrow path to good? or will she slap him silly?'
    )

    movie8= add_movie(
        characters=[characters[2], characters[3], characters[4]],
        genres=[biography, animation],
        title='Ants in your pant',
        year=2011,
        producer=new_producer6,
        summary='A Biography abut people who cant sit still since they have ants in their pants'
                ' The documentary also looks at liers whos pants are on fire'
                ' As well as a brief overview of a dance crew with bees on their knees.'
    )

    movie9 = add_movie(
        characters=[characters[0]],
        genres=[mystery],
        title='Testing, 1.2.3 Testing',
        year=2010,
        producer=new_producer6,
        summary='This mystery will have you questioning your life.'
                ' Will the tests pass or wont they?'
                ' What happens if the mic doesnt work? Will the show go on?'
    )

    movie10 = add_movie(
        characters=[characters[4], characters[3], characters[1], characters[5]],
        genres=[adventure, fantasy],
        title='Rub a Dub Dub',
        year=2015,
        producer=new_producer3,
        summary='Rub a dub dub,'
                ' Three fools in a tub,'
                ' And who do you think they be?'
                ' The butcher, the baker,'
                ' The candlestick maker.'
                ' Turn them out, knaves all three'
    )




if __name__ == '__main__':
    print "Starting Movies population script..."
    populate()
