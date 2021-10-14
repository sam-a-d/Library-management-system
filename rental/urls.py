from django.urls import path, include
from . import views

urlpatterns = [
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('process_order/', views.processOrder, name='processOrder'),
    path('update/', views.update_cart, name='update_cart'),
]
