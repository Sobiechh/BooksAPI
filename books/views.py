from django.shortcuts import render, redirect

from api.models import Book
from books.filters import BookFilter
from books.forms import BookForm


def books_list(request):
    books = Book.objects.all()

    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs

    context = {
        'books': books,
        'filter': book_filter,
    }

    return render(request, 'books_list/index.html', context)


def new(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()

    context = {
        'form': form,
    }

    return render(request, 'book_new/index.html', context)


def edit(request, pk):
    book = Book.objects.get(book_id=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    context = {
        'form': form,
        'book': book,
    }

    return render(request, 'book_edit/index.html', context)


def welcome(request):
    return render(request, "welcome/index.html")
