from django.urls import path, include
from . import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path('all_books/', views.BookListView.as_view(template_name="admin/book_list.html"), name='all_books'),
]
