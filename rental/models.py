from django.db import models
from django.db import models


from user.models import User
from root.models import Book


# Create your models here.
class Order(models.Model):
    """Model definition for Order."""

    order_status = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    )
    # TODO: Define fields here
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    order_date = models.DateTimeField(auto_now_add=True, null=True)
    status = models.TextField(default="Pending", choices=order_status)
    order_placed = models.BooleanField(default=False)
    payment_done = models.BooleanField(default=False, null=True)
    payMethod = models.CharField(max_length=20, null=True, blank=True)
    transaction_id = models.CharField(
        max_length=100, default='', blank=True, null=True)
    transaction_phone = models.CharField(
        max_length=20, default='', blank=True, null=True)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    # def __str__(self):
    #     """Unicode representation of Order."""
    #     return self.str(user_id)

    @property
    def get_delivered_status():
        return self.order_status == 'Delivered'

    @property
    def get_cart_items(self):
        ordered_books = self.orderitem_set().all()
        return self.ordered_books


class OrderItem(models.Model):
    """Model definition for OrderItem."""

    # TODO: Define fields here
    order = models.ForeignKey(Order, null=True, on_delete=models.SET_NULL)
    book = models.ForeignKey(Book, null=True, on_delete=models.SET_NULL)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for OrderItem."""

        verbose_name = 'OrderItem'
        verbose_name_plural = 'OrderItems'

    def __str__(self):
        """Unicode representation of OrderItem."""
        return self.book.name


class Shipping(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    # shipping ship_
    ship_address = models.TextField(null=True, default="", blank=True)
    ship_district = models.CharField(max_length=150, null=True, blank=True)
    ship_upazilla = models.CharField(max_length=150, null=True, blank=True)
    ship_postcode = models.CharField(max_length=10, null=True, blank=True)
    ship_phone = models.CharField(max_length=20, null=True, blank=True)
