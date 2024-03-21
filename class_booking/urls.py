from django.urls import path
from . import views
from class_booking.views import cancel_booking


urlpatterns = [
    path('', views.class_booking_form, name='booking'),
    path('cancel/booking/<int:booking_id>/', cancel_booking, name='cancel_booking'),
]