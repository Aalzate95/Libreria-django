from django.shortcuts import render
from . import models, serializers
from rest_framework import viewsets
# Create your views here.

class BookViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.BookSerializer

    def get_queryset(self):
        book = models.Book.objects.all()
        return book
