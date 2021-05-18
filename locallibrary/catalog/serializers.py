from rest_framework.serializers import ModelSerializer, ImageField

from . import models

class BookSerializer(ModelSerializer):
    class Meta:
        model = models.Book
        fields = ["id", "title", "author", "summary"]

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = models.Author
        fields = ["id","first_name","last_name","date_of_birth","date_of_death"]