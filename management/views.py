from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
# import generic views
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from root.models import Book, Author, Publisher
from root.filters import BookFilter
from  user.decorators import admin_only_access

from .filters import ListViewWithFilter
# Create your views here.

@method_decorator(admin_only_access, name='dispatch')
class BookListView(ListViewWithFilter):
    model = Book
    context_object_name = 'books'
    target_filter = BookFilter


@method_decorator(admin_only_access, name='dispatch')
class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('all_books')
        
@method_decorator(admin_only_access, name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'

    def get_success_url(self):
        return reverse('all_books')


@method_decorator(admin_only_access, name='dispatch')
class AuthorCreateView(CreateView):
    model = Author
    fields = '__all__'

    def get_success_url(self):
        return reverse('all_books')

@method_decorator(admin_only_access, name='dispatch')
class AuthorUpdateView(UpdateView):
    model = Author
    fields = '__all__'

    def get_success_url(self):
        return reverse('all_books')

@method_decorator(admin_only_access, name='dispatch')
class PublisherCreateView(CreateView):
    model = Publisher
    fields = '__all__'

    def get_success_url(self):
        return reverse('all_books')