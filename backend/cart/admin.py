from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.


admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Country)
admin.site.register(Region)