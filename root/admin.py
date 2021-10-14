from django.contrib import admin

# Register your models here.

from .models import *
from user.models import *
from rental.models import Order

admin.site.register(Book)
admin.site.register(Natinality)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Publisher)
admin.site.register(Author)

admin.site.register(Order)
admin.site.register(Member)
admin.site.register(Division)
