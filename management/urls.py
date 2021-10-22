from django.urls import path, include
from . import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path('all_books/', views.BookListView.as_view(template_name="management/book_list.html"), name='all_books'),
    path('book/add/', views.BookCreateView.as_view(template_name="management/mgt_generic.html"), name='book-add'),
    path('book/update/<int:pk>', views.BookUpdateView.as_view(template_name="management/mgt_generic.html"), name='book-update'),
    path('author/update/<int:pk>', views.AuthorUpdateView.as_view(template_name="management/mgt_generic.html"), name='author-update'),
]
