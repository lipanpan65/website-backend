from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from user.models import UserInfo


# Create your views here.


class UserInfoView(ModelViewSet):
    """用户"""
    queryset = UserInfo.objects.all()

    def register(self, request, *args, **kwargs):
        """注册"""
        username = request.data.get("username")
        password = request.data.get("password")
        if username and password:
            username = self.queryset.filter(username=username)

    def login(self, request, *args, **kwargs):
        """登录"""
        pass
