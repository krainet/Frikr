# -*- coding: utf-8 -*-
from rest_framework.response import Response
__author__ = 'hadock'
from django.contrib.auth.models import User
from rest_framework.views import APIView
from users.serializers import UserSerializer



class UserListAPI(APIView):
    def get(self,req):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        serialized_users = serializer.data # en data van los datos...
        return Response(serialized_users)
