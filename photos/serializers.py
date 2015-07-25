# -*- coding: utf-8 -*-
from photos.models import Photo

__author__ = 'hadock'
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        read_only_fields = ('owner',)

class PhotoListSerializer(PhotoSerializer):
    class Meta(PhotoSerializer.Meta):  # ojo a heredar correctamente la clase meta también!!!!
        fields = ('id', 'name', 'url')
