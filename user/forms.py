from django.forms import ModelForm
from .models import Member


class UserProfileUpdateForm(ModelForm):
    """Form definition for UserProfileUpdate."""

    class Meta:
        """Meta definition for UserProfileUpdateform."""

        model = Member
        fields = '__all__'
        exclude = ['user', 'national_id_no', 'library_card_no']
