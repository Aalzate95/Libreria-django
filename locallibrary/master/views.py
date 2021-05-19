from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from django.contrib.auth.models import User
from . import models, serializers
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

#class RegisterView(generics.CreateAPIView):
class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer