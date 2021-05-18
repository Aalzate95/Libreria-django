from rest_framework.serializers import ModelSerializer, ImageField

from . import models

class BookSerializer(ModelSerializer):

    class Meta:
        model = models.Book
        fields = ["id", "title", "author", "summary"]