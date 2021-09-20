from rest_framework import viewsets

from .models import Book, Author, ISBN
from .serializers import BookSerializer, AuthorSerializer, IsbnSerializer


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class AuthorViewset(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class IsbnViewset(viewsets.ModelViewSet):
    serializer_class = IsbnSerializer
    queryset = ISBN.objects.all()
