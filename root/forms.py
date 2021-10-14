from django.forms import ModelForm
from rental.models import Order


class OrderForm(ModelForm):
    """Form definition for Order."""

    class Meta:
        """Meta definition for Orderform."""

        model = Order
        fields = '__all__'
