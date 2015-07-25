# -*- coding: utf-8 -*-
from django.core.exceptions import ValidationError
from frikr.settings import BADWORDS

__author__ = 'hadock'

def badwords_detector(value):
    """
    Validador de BADWORDS
    :param value: string
    :return: true if correct , else lanza excepcion
    """
    for badword in BADWORDS:
        # ojo a los unicodes al comparar strings NO unicode (peta)
        if badword.lower() in value.lower():
            raise ValidationError(u'La palabra {0} no está permitida'.format(badword))

    # si todo OK devuelvo datos limpios o normalizados
    return True