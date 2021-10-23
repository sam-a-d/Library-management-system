from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

# from user.models import Order
from rental.models import Order
from user.models import User
from user.decorators import allowed_users, admin_only_access

from .models import *
from .forms import OrderForm
from .filters import OrderFilter, BookFilter


# Create your views here.


def home(request):

    books = Book.objects.filter(stock_availability=True)
    me = "Samad"
    book_filter = BookFilter(request.GET, queryset=books)
    context = {
        'book_filter': book_filter,
    }
    return render(request, 'home.html', context)


def books(request):

    books = Book.objects.filter(stock_availability=True)
    genres = Genre.objects.all()

    book_filter = BookFilter(request.GET, queryset=books)
    books = book_filter.qs
    context = {
        'books': books,
        'genres': genres,
        'book_filter': book_filter,
    }

    return render(request, 'books.html', context)


@login_required(login_url='login')
# @allowed_users(allowed_groups=['admin'])
@admin_only_access
def orders(request):
    orders = Order.objects.filter(order_placed=True).order_by("-order_date")
    totoal_customer = User.objects.all().count()
    totoal_book = Book.objects.all().count()
    total_order = orders.count()
    total_delivered = Order.objects.filter(status="Delivered").count()
    total_pending = Order.objects.filter(status="Pending").count()

    order_filter = OrderFilter(request.GET, queryset=orders)
    orders = order_filter.qs

    context = {
        'orders': orders, 'total_order': total_order,
        'total_delivered': total_delivered,
        'total_pending': total_pending,
        'total_customer': totoal_customer,
        'totoal_book': totoal_book,
        'order_filter': order_filter
    }

    return render(request, 'orders.html', context)


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['admin'])
def user(request, user_id):
    user = User.objects.get(id=user_id)
    orders = user.order_set.all()
    order_delivered = user.order_set.filter(status='Delivered').count()
    order_count = orders.count()

    context = {'user': user, 'orders':  orders,
               'order_count': order_count, 'order_delivered': order_delivered}

    return render(request, 'user.html', context)


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['admin'])
def create_order(request):

    form = OrderForm()

    if request.method == "POST":
        # print("Post Request", request.POST)
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'OrderForm': form}
    return render(request, 'order_form.html', context)


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['admin'])
def update_order(request, order_id):

    order = Order.objects.get(id=order_id)
    form = OrderForm(instance=order)

    if request.method == "POST":
        # print("Post Request", request.POST)
        form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            return redirect('orders')

    context = {'OrderForm': form}
    return render(request, 'order_form.html', context)


@ login_required(login_url='login')
@ allowed_users(allowed_groups=['admin'])
def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    user = order.user_id.username
    if request.method == "POST":
        order.delete()
        return redirect('orders')

    context = {'order': order, 'user': user}
    return render(request, 'delete.html', context)


class AuthorListView(ListView):
    model = Author
    template_name="book/authorList.html"

class PublisherListView(ListView):
    model = Publisher
    template_name="book/publisherList.html"
    
class GenreListView(ListView):
    model = Genre
    template_name="book/genreList.html"

class AuhtorDetailView(DetailView):
    model = Author
    template_name = 'book/authorDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(author=self.kwargs.get('pk'))
        return context

class PublisherDetailView(DetailView):
    model = Publisher
    template_name = 'book/publisherDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(publisher=self.kwargs.get('pk'))
        return context


class GenreDetailView(DetailView):
    model = Genre
    template_name = 'book/genreDetails.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.filter(genre=self.kwargs.get('pk'))
        return context

    