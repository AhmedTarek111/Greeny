from django.contrib import admin
from .models import Profile,DeliveryAddress,ContactNumber

admin.site.register(Profile)
admin.site.register(DeliveryAddress)
admin.site.register(ContactNumber)