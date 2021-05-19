from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.authentication import SessionAuthentication

# Create your views here.

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    #authentication_classes=[SessionAuthentication]
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        book = models.Book.objects.all()
        return book

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        author = models.Author.objects.all()
        return author