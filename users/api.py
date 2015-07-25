# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.http import HttpResponse
from users.serializers import UserSerializer
# importo json render
from rest_framework.renderers import JSONRenderer
__author__ = 'hadock'
from django.views.generic import View

class UserListAPI(View):
    def get(self,req):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data # en data van los datos...
        renderer = JSONRenderer()
        json_users = renderer.render(serialized_users)
        return HttpResponse(json_users)
