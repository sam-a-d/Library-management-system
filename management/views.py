from django.shortcuts import render

from root.views import Book

# import generic views
from django.views.generic import ListView



# Create your views here.

class BookListView(ListView):
    model = Book
    context_object_name = 'books'