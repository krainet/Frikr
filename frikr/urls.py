
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from photos.api import PhotoListAPI,PhotoDetailAPI
from photos.views import HomeView, PhotoDetailView, PhotoCreateView, PhotoListView, UserPhotosView
from users.api import UserListAPI, UserDetailAPI
from users.views import LoginView, LogoutView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #urls photos
    # old home URL: url(r'^$', 'photos.views.home', name='photos_home'),
    url(r'^$', HomeView.as_view(), name='photos_home'),
    url(r'detail/(?P<id>[0-9]+)$', PhotoDetailView.as_view(), name='photos_detail'),
    url(r'^photos/$', PhotoListView.as_view(), name='photo_list'),
    url(r'^my-photos/$', login_required(UserPhotosView.as_view()), name='user_photos'), #protegemos con decorator de login
    url(r'^photos/new$', PhotoCreateView.as_view(), name='photo_create'),

    # url(r'^.*$', 'photos.views.home'), wildcard
    # Users url
    # old login url: url(r'^login$', 'users.views.login', name='users_login'),
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
    url(r'^prueba$', 'users.views.prueba', name='users_prueba'),


    # urls api users
    url(r'^api/1.0/users/$', UserListAPI.as_view(), name='user_list_api'),
    url(r'^api/1.0/users/(?P<pk>[0-9]+)$', UserDetailAPI.as_view(), name='user_detail_api'),

    # url api photos
    url(r'^api/1.0/photos/$', PhotoListAPI.as_view(), name='photo_list_api'),
    url(r'^api/1.0/photos/(?P<pk>[0-9]+)$', PhotoDetailAPI.as_view(), name='photo_detail_api')

]
