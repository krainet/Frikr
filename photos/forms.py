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

    def clean(self):
        """
        Validar si contiene tacos
        :return: diccionario con attr OK
        """
        cleaned_data = super(PhotoForm, self).clean()
        description = cleaned_data.get('description', '')

        for badword in BADWORDS:
            # ojo a los unicodes al comparar strings NO unicode (peta)
            if badword.lower() in description.lower():
                raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

        # si todo OK devuelvo datos limpios o normalizados
        return cleaned_data
