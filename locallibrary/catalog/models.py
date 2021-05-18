from django.db.models import Model, CASCADE, DO_NOTHING,SET_NULL
from django.db.models import ForeignKey, OneToOneField, ManyToManyField
import uuid # Requerida para las instancias de libros únicos
from django.db.models import (
    CharField,
    IntegerField,
    FloatField,
    DateTimeField,
    BooleanField,
    FileField,
    UUIDField,
    DateField
)
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.


class Book(Model):
    title = CharField(max_length=200)
    author = ForeignKey("Author", on_delete=SET_NULL, null=True)
    summary = CharField(max_length=1000, help_text="Ingrese una descripción del libro")
    imprint = CharField
    isbn = CharField('ISBN',max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = ManyToManyField("Genre", help_text="Seleccione un genero para este libro")
    language = ForeignKey('Language', on_delete=SET_NULL, null=True)

    class Meta:
        ordering = ["-title"]

    def __str__(self):
        return f"{self.title}"
        
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])

    display_genre.short_description = 'Genre'


class BookInstance(Model):
    """
    Modelo que representa una copia específica de un libro (i.e. que puede ser prestado por la biblioteca).
    """
    id = UUIDField(primary_key=True, default=uuid.uuid4, help_text="ID único para este libro particular en toda la biblioteca")
    book = ForeignKey('Book', on_delete=SET_NULL, null=True)
    imprint = CharField(max_length=200)
    due_back = DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Disponibilidad del libro')

    class Meta:
        ordering = ["due_back"]


    def __str__(self):
        """
        String para representar el Objeto del Modelo
        """
        return '%s (%s)' % (self.id,self.book.title)


class Genre(Model):
    name = CharField(max_length=200,help_text="Ingrese el nombre del genero (p. ej. Ciencia Ficción, Romance, etc.).")

    def __str__(self):
        return f"{self.name}"


class Author(Model):
    """
    Modelo que representa un autor
    """
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)
    date_of_birth = DateField(null=True, blank=True)
    date_of_death = DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        """
        String para representar el Objeto Modelo
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Language(Model):
    """
    Modelo que representa el lenguaje en el que está escrito un libro
    """
    name = CharField(max_length=200,help_text="Ingrese el lenguaje natural del libros (p. ej. Español, Ingles, Frances, etc.).")

    def __str__(self):
        return f"{self.name}"