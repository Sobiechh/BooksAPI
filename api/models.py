from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    authors = models.ManyToManyField("Author", blank=True)
    published_date = models.DateField()
    isbns = models.ManyToManyField("ISBN", blank=True)
    page_count = models.IntegerField()
    book_cover_link = models.CharField(max_length=255, blank=True)
    publication_language = models.CharField(max_length=255, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=255, blank=True)


class ISBN(models.Model):
    isbn_id = models.CharField(max_length=255, unique=True, primary_key=True)
    type = models.CharField(max_length=255, blank=True)
