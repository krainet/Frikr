# -*- coding: utf-8 -*-
from rest_framework.response import Response
__author__ = 'hadock'
from photos.models import Photo
from rest_framework.views import APIView
from photos.serializers import PhotoSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status


class PhotoListAPI(APIView):
    def get(self, req):
        photos = Photo.objects.all()
        serializer = PhotoSerializer(photos, many=True)
        return Response(serializer.data)


class PhotoDetailAPI(APIView):

    def get(self, req, pk):
        photo = get_object_or_404(Photo, pk=pk)
        return Response(PhotoSerializer(photo).data)

