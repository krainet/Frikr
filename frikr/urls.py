
from django.conf.urls import include, url
from django.contrib import admin
from photos.views import HomeView
from users.views import LoginView
from users.views import LogoutView
from photos.views import PhotoDetailView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #urls photos
    # old home URL: url(r'^$', 'photos.views.home', name='photos_home'),
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'detail/(?P<id>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^photos/new$', 'photos.views.create', name='photo_create'),

    # url(r'^.*$', 'photos.views.home'), wildcard
    # Users url
    # old login url: url(r'^login$', 'users.views.login', name='users_login'),
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^prueba$', 'users.views.prueba', name='users_prueba')
]
