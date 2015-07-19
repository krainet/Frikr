# -*- coding: utf-8 -*-
__author__ = 'hadock'

from django.conf import settings

COPYRIGHT = 'RIG'
COPYLEFT = 'LEFT'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'Copyleft'),
    (CREATIVE_COMMONS, 'Creative Commons')
)

LICENSES = getattr(settings, 'LICENCES', DEFAULT_LICENSES)

BADWORDS = getattr(settings, 'BADWORDS', [])
