
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from .custom_serializers import *
from rest_framework.response import Response

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')



class UserViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DummyViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for return a dummy dict response.
    """
    

    def list(self, request):
        dummy = {'key1':'value1','key2':'value2'}
        return Response(dummy)

    def post(self, request):
        print 'in post'
        return Response({'success':True})