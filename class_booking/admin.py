from django.contrib import admin
from .models import ClassDetail, Booking

# Register your models here.

"""
Admin configuration for managing Class Detail and Booking models.
"""
admin.site.register(ClassDetail)
admin.site.register(Booking)
