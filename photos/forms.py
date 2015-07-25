# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from photos.settings import BADWORDS

__author__ = 'hadock'
from django import forms
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['owner']
