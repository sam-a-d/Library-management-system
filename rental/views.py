from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import json

from root.models import Book
from user.models import Member
from user.decorators import *

from .models import Order, OrderItem, Shipping


# Create your views here.

@authenticated_user
def cart(request):
    # us = request.user

    # orders = Order.objects.filter(user_id=us.id, complete=False)

    if request.user.is_authenticated:
        current_user = request.user
        # if len(current_user.order_set.all()) >= 1:
        #     orders = current_user.order_set.all()[0]
        #     cartItems = orders.orderitem_set.all()
        # else:
        #     cartItems = ''

        current_user = request.user
        orders, created = Order.objects.get_or_create(
            user_id=current_user, order_placed=False)

        print(orders)
        cartItems = orders.orderitem_set.all()

        context = {
            'cartItems': cartItems
        }
        return render(request, 'rental/cart.html', context)

    else:
        return redirect('login')


@authenticated_user
def update_cart(request):
    data = json.loads(request.body)

    productId = data["productId"]
    action = data['action']

    current_user = request.user
    member = current_user.member
    book = Book.objects.get(id=productId)

    order, created = Order.objects.get_or_create(
        user_id=current_user, order_placed=False)

    orderItem, created = OrderItem.objects.get_or_create(
        order=order, book=book)

    orderItem.save()

    if action == 'remove':
        orderItem.delete()

    message = ""

    if action == 'add':
        # message = "Book has been removed"

        if created:
            message = "Book has been added to your CART"
        else:
            message = "Book is already in your CART"

    return JsonResponse(message, safe=False)


@authenticated_user
def checkout(request):
    current_user = request.user
    current_order, created = Order.objects.get_or_create(
        user_id=current_user, order_placed=False)

    # if len(current_user.order_set.all()) >= 1:
    #     orders = current_user.order_set.all()[0]
    #     cartItems = orders.orderitem_set.all()
    # else:
    #     cartItems = ''

    cartItems = current_order.orderitem_set.all()
    context = {
        'cartItems': cartItems,
    }

    return render(request, 'rental/checkout.html', context)


@authenticated_user
def processOrder(request):

    data = json.loads(request.body)

    # current user and the order
    current_user = request.user
    current_order = Order.objects.get(
        user_id=current_user.id, order_placed=False)

    # Shipping details from from end
    ship_address = data['shippingInfo']['address']
    ship_district = data['shippingInfo']['district']
    ship_upazilla = data['shippingInfo']['upazilla']
    ship_postcode = data['shippingInfo']['postcode']
    ship_phone = data['shippingInfo']['phone']

    # order details from front end
    order_payment_method = data['shippingInfo']['payment']
    order_payment_transaction_id = data['shippingInfo']['transaction_id']
    order_payment_phone = data['shippingInfo']['transaction_phone']

    # update the order table
    current_order.order_placed = True
    current_order.payMethod = order_payment_method
    current_order.transaction_id = order_payment_transaction_id
    current_order.transaction_phone = order_payment_phone

    # Make the book(s) unavailable imidiately when someone placed an order for that book(s)
    for item in current_order.orderitem_set.all():
        item.book.stock_availability = False
        item.book.save()

    current_order.save()

    return JsonResponse('Form submitted!', safe=False)
