from django.db import models


class Book(models.Model):
    book_id = models.CharField(max_length=255, unique=True, primary_key=True)
    title = models.CharField(max_length=255, blank=True)
    authors = models.ManyToManyField("Author", blank=True)
    published_date = models.DateField(blank=True, null=True)
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
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.isbn_id}'
