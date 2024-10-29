from django.contrib import admin
from .models import Barber,BarberShop,Customer

# Register your models here.
admin.site.register(Barber)
admin.site.register(BarberShop)
admin.site.register(Customer)
