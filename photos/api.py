# -*- coding: utf-8 -*-
from photos.serializers import PhotoSerializer, PhotoListSerializer

__author__ = 'hadock'
from photos.models import Photo
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class PhotoListAPI(ListCreateAPIView):
    queryset = Photo.objects.all()
    # serializer_class = PhotoListSerializer

    # Al sobreescribir este método podemos usar un serializador u otro en funcion del metodo de la vista generica ListCreateApiView
    def get_serializer_class(self):
        return PhotoSerializer if self.request.method == 'POST' else PhotoListSerializer


class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
