# -*- coding: utf-8 -*-
from photos.models import Photo

__author__ = 'hadock'
from rest_framework import serializers

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo