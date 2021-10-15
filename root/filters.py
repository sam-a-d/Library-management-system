import django_filters
from .models import Book
from rental.models import Order
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):

    user_id__id = django_filters.CharFilter(lookup_expr='iexact')
    book_id__id = django_filters.CharFilter(lookup_expr='iexact')
    user_id__email = django_filters.CharFilter(lookup_expr='iexact')
    start_date = DateFilter(field_name='order_date', lookup_expr='gte')
    end_date = DateFilter(field_name='order_date', lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['order_date', 'book_id', 'user_id']


class BookFilter(django_filters.FilterSet):

    class Meta:
        model = Book
        fields = ['author', 'genre', 'publisher', 'language']
