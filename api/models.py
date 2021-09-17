from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    authors = models.ManyToManyField("Author", blank=True)
    published_year = models.IntegerField(blank=True)
    isbns = models.ManyToManyField("ISBN", blank=True)
    page_count = models.IntegerField(blank=True)
    book_cover_link = models.CharField(max_length=255, blank=True)
    publication_language = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.title}'


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.name}'


class ISBN(models.Model):
    isbn_id = models.CharField(max_length=255, unique=True, primary_key=True)
    type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.type}'
