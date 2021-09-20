from django.shortcuts import render, redirect

from api.models import Book
from books.filters import BookFilter
from books.forms import BookForm, ImportForm
from books.importer import BooksImporter


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


def import_by_keyword(request):
    if request.method == 'POST':
        form = ImportForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            url = f'https://www.googleapis.com/books/v1/volumes?q={keyword}'
            BooksImporter(url).import_books()

            return redirect('books')
    else:
        form = ImportForm()

    context = {
        'form': form,
    }

    return render(request, 'books_import_by_keyword/index.html', context)


def welcome(request):
    return render(request, "welcome/index.html")
