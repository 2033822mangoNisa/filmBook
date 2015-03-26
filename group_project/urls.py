from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from django.conf.urls.static import static
from django.conf import settings


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/movies/user/' + user.username + '/profile_registration/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'group_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('movies.urls')),
    url(r'^movies/', include('movies.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
