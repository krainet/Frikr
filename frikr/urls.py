from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', 'photos.views.home', name='photos_home'),
    url(r'detail/(?P<id>[0-9]+)$', 'photos.views.detail', name='photos_detail'),
    url(r'^photos/new$', 'photos.views.create', name='photo_create'),

    # url(r'^.*$', 'photos.views.home'), wildcard
    # Users url
    url(r'^login$', 'users.views.login', name='users_login'),
    url(r'^logout$', 'users.views.logout', name='users_logout'),
    url(r'^prueba$', 'users.views.prueba', name='users_prueba')
]
