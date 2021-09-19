from django.urls import path

from . import views

urlpatterns = [
    path('books', views.books_list, name='books'),
    path('', views.welcome, name='welcome'),
    path('new', views.new, name='new'),
    path('edit/<str:pk>', views.edit, name='edit'),
]
