from django.test import TestCase
from django.contrib.auth.models import User
from movies.models import Movie, Genre, Actor, Producer, Comment, UserProfile, Notification, MovieRating, Character


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


class GenreTestCase(TestCase):
    def setUp(self):
        Genre.objects.create(name='TestGenre')

    def test_genre_name_and_slug(self):
        genre = Genre.objects.get(name='TestGenre')
        self.assertEqual(genre.name, 'TestGenre')
        self.assertEqual(genre.slug, 'testgenre')


class UserProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.get_or_create(username='testuser1', email='test@test.com')[0]
        user.set_password('testpass')
        user.save()

    def test_default_picture(self):
        user = User.objects.get(username='testuser1')
        user_profile = UserProfile.objects.get_or_create(user=user, first_name='fname', last_name='lname', type=1)[0]
        self.assertEqual(user_profile.picture.url, '/media/profile_images/default_user_picture.jpg')


class MovieTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.get_or_create(username='testuser1', email='test@test.com')[0]
        user1.set_password('testpass')
        user1.save()

        user2 = User.objects.get_or_create(username='testuser2', email='test2@test.com')[0]
        user2.set_password('testpass')
        user2.save()

        user_profile1 = UserProfile.objects.get_or_create(user=user1, first_name='fname', last_name='lname', type=3)[0]
        user_profile2 = UserProfile.objects.get_or_create(user=user2, first_name='fname', last_name='lname', type=2)[0]
        producer = Producer.objects.get_or_create(user=user_profile1, first_name=user_profile1.first_name,
                                            last_name=user_profile1.last_name)[0]
        actor = Actor.objects.get_or_create(user=user_profile2, name=user_profile2.first_name,
                                            last_name=user_profile2.last_name)[0]
        character = add_char('Character1', actor)

        genre1 = add_genre('Drama')
        genre2 = add_genre('Action')

        add_movie(
            characters=[character],
            genres=[genre1, genre2],
            title='Test Movie',
            year=2015,
            producer=producer
        )

    def test_movie_slug(self):
        movie = Movie.objects.get(title='Test Movie')
        self.assertEqual(movie.slug, 'test-movie')

    def test_movie_genres(self):
        movie = Movie.objects.get(title='Test Movie')
        genre1 = Genre.objects.get(name='Drama')
        genre2 = Genre.objects.get(name='Action')

        self.assertEqual(genre1, movie.genres.all()[0])
        self.assertEqual(genre2, movie.genres.all()[1])

    def test_movie_character(self):
        movie = Movie.objects.get(title='Test Movie')
        character = Character.objects.get(name='Character1')

        self.assertEqual(character, movie.characters.all()[0])

    def test_movie_get_actors(self):
        movie = Movie.objects.get(title='Test Movie')
        actor = Actor.objects.get(name='fname')

        self.assertEqual(actor, movie.get_actors()[0])

    def test_movie_get_rating(self):
        movie = Movie.objects.get(title='Test Movie')
        user = User.objects.get(username='testuser1')
        user_profile = UserProfile.objects.get(user=user)
        rating = MovieRating.objects.get_or_create(user=user_profile, movie=movie, rating=7.0)

        self.assertEqual(7.0, movie.get_rating()['rating'])
        self.assertEqual(1, movie.get_rating()['ratings_no'])


