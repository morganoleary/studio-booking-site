from . import views
from django.urls import path

urlpatterns = [
    path('', views.class_booking_form, name='booking'),
]