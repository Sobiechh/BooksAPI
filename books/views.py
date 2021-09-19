from django.shortcuts import render

from api.models import Book
from books.filters import BookFilter


def books_list(request):
    books = Book.objects.all()

    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs

    context = {
        'books': books,
        'filter': book_filter,
    }

    return render(request, 'books_list/index.html', context)


def welcome(request):
    return render(request, "welcome/index.html")
