# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photos', '0002_auto_20150717_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='owner',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='photo',
            name='visibility',
            field=models.CharField(default=b'PUB', max_length=4, choices=[(b'PUB', b'P\xc3\xbablica'), (b'PRIV', b'Privada')]),
        ),
    ]
