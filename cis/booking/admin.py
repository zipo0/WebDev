from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Shelf, Reservation

admin.site.register(Shelf)
admin.site.register(Reservation)
