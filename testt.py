import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'group_project.settings')

import django
django.setup()

from movies.models import UserProfile, Actor, Producer, Movie
from django.contrib.auth.models import User

for movie in Movie.objects.all():
    print movie, ' - ', movie.user

user = User.objects.get(username='joker')
profile = UserProfile.objects.get(user=user)
print Movie.objects.filter(user=profile)