from django.shortcuts import render

from api.models import Book


def books_list(request):
    return render(request, "books_list.html",
                  {"books": Book.objects.all()}
                  )


def welcome(request):
    return render(request, "welcome/index.html")
