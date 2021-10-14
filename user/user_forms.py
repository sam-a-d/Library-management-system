from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms


class CustomUserCreationForm(UserCreationForm):
    """Model definition for CreateUserform."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for CreateUserform."""

        model = User
        fields = ['username', 'email', 'password1', 'password2']
