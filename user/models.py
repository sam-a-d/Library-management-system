from django.db import models
from root.models import Book
from django.contrib.auth.models import User


# Create your models here.


class Division(models.Model):
    """Model definition for Division."""

    # TODO: Define fields here
    name = models.CharField(max_length=40, null=True)

    class Meta:
        """Meta definition for Division."""

        verbose_name = 'Division'
        verbose_name_plural = 'Divisions'

    def __str__(self):
        """Unicode representation of Division."""
        return self.name


class Member(models.Model):
    """Model definition for Member."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # TODO: Define fields here
    genders = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    library_card_no = models.IntegerField(null=True, blank=True)

    profile_picture = models.ImageField(
        null=True, blank=True, default='d_image.jpeg')
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=30, null=True, choices=genders)
    profession = models.CharField(max_length=50, null=True, default='')
    phone_number = models.IntegerField(null=True)
    facebook_profile = models.CharField(max_length=120, null=True)
    national_id_no = models.IntegerField(null=True)
    addr_division = models.ForeignKey(
        Division, null=True, on_delete=models.SET_NULL)
    addr_District = models.CharField(max_length=40, null=True)
    addr_thana = models.CharField(max_length=40, null=True)
    postcode = models.IntegerField(null=True)
    word_no = models.IntegerField(null=True)
    house_no = models.IntegerField(null=True, blank=True)

    acc_creation_date = models.DateField(auto_now_add=True, null=True)

    class Meta:
        """Meta definition for Member."""

        verbose_name = 'Member'
        verbose_name_plural = 'Members'

    def __str__(self):
        """Unicode representation of Member."""
        return self.user.username
