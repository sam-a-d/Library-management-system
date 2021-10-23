
from django.urls import path, include
from . import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path('', views.home, name='home'),
    path('user/', include('user.urls')),
    path('email/', include(email_urls)),
    path('books/', views.books, name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('publisher/', views.PublisherListView.as_view(), name='publisher'),
    path('catalog/', views.GenreListView.as_view(), name='catalog'),
    path('orders/', views.orders, name='orders'),
    path('user/<str:user_id>/', views.user, name='user'),
    path('create_order/', views.create_order, name='create_order'),
    path('update_order/<str:order_id>', views.update_order, name='update_order'),
    path('delete_order/<str:order_id>', views.delete_order, name='delete_order'),
]
