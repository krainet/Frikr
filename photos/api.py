# -*- coding: utf-8 -*-
from photos.serializers import PhotoSerializer
__author__ = 'hadock'
from photos.models import Photo
from rest_framework.generics import ListCreateAPIView


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
