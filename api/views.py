from rest_framework import viewsets

from .filters import BookFilter
from .models import Book, Author, ISBN
from .serializers import BookSerializer, AuthorSerializer, IsbnSerializer


class BookViewset(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    filter_class = BookFilter
    queryset = Book.objects.all()


class AuthorViewset(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class IsbnViewset(viewsets.ModelViewSet):
    serializer_class = IsbnSerializer
    queryset = ISBN.objects.all()
