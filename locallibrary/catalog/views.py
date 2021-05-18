from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
# Create your views here.

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        book = models.Book.objects.all()
        return book

class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.AuthorSerializer

    def get_queryset(self):
        author = models.Author.objects.all()
        return author