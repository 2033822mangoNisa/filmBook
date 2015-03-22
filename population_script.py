import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

from movies.models import UserProfile, Actor, Producer
from django.contrib.auth.models import User


# to add a user
new_user = User.objects.get_or_create(username="some_username", email="emailaddres@adsas.com")[0]
new_user.set_password("some_password")
new_user.save()


# to add a user profile for a user
# the 'type' attribute can be either 1, 2 or 3
# 1 is for regular user
# 2 is for Actor (so the user is an actor)
# 3 is for Producer
# you should make them all type=1 at first and then change them later for some users
# when you make the Actor and Producer objects
new_user_profile = UserProfile.objects.get_or_create(first_name="fname", last_name='lname',
                                                     info='a short description about the user', type=1)


# and now to add some Actors and Producers
# for the 'user' field you have to use a UserProfile object that was created in the previous step
# the 'available' field can be 'yes' or 'no' and it indicates if the actor is available to play in movies or not
# the 'name' and 'last_name' fields will be the same as those of the UserProfile that is linked to it
# the 'info' and 'link' fields are optional so you can add them to some of the users and you can omit them for others
new_actor = Actor.objects.get_or_create(user=new_user_profile, name=new_user_profile.first_name,
                                        last_name=new_user_profile.last_name, info='some description for the actor',
                                        link='a link, like the personal website of the actor or something like it')


# now add some Producers
# it's the same as above, for Actor as it has almost the same fields
new_producer = Producer.objects.get_or_create(user=new_user_profile, name=new_user_profile.first_name,
                                        last_name=new_user_profile.last_name, info='some description for the actor',
                                        link='a link, like the personal website of the actor or something like it')


# so at this point we now have in the database some regular users, some Actors and some Producers
# so now we can start adding movies
# the names of the actors, producers and movies should be fictional because now the website purpose is not as before
# now it should promote amateur producers and actors and help them





