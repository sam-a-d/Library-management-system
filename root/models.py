from django.db import models

# Create your models here.


class Genre(models.Model):
    """Model definition for Genre."""

    # TODO: Define fields here
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Natinality(models.Model):
    """Model definition for Nationality."""

    # TODO: Define fields here
    country = models.CharField(max_length=30)

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Natinality'
        verbose_name_plural = 'Natinalities'

    def __str__(self):
        return self.country


class Language(models.Model):
    """Language of the book ."""

    # TODO: Define fields here
    language = models.CharField(max_length=30)

    def __str__(self):
        return self.language


class Publisher(models.Model):
    """Model definition for Publisher."""

    # TODO: Define fields here
    name = models.CharField(max_length=60)
    country = models.ForeignKey(
        Natinality, null=True, on_delete=models.SET_NULL)
    date_estd = models.DateField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    """Model definition for Author."""

    # TODO: Define fields here
    name = models.CharField(max_length=60)
    natinality = models.ForeignKey(
        Natinality, null=True, on_delete=models.SET_NULL)
    date_of_birth = models.DateField()
    biography = models.TextField()

    class Meta:
        """Meta definition for Order."""

        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Book(models.Model):

    library_book_no = models.IntegerField()

    name = models.CharField(max_length=60)

    stock_availability = models.BooleanField(default=True)

    # ForeignKey start
    author = models.ForeignKey(
        Author, null=True, on_delete=models.SET_NULL)
    publisher = models.ForeignKey(
        Publisher, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(
        Genre, null=True, on_delete=models.SET_NULL)
    language = models.ForeignKey(
        Language, null=True, on_delete=models.SET_NULL)
    # ForeignKey end

    photo = models.ImageField(null=True, blank=True)
    edition = models.CharField(max_length=60, blank=True, default='')
    pages = models.IntegerField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    isbn = models.CharField(max_length=60, null=True, blank=True, default='')
    sh_description = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')

    def __str__(self):
        return self.name
