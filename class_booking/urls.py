from . import views
from django.urls import path

urlpatterns = [
    path('class_booking/', views.booking, name='booking')
]