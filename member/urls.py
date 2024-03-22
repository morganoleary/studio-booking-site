from django.urls import path
from . import views

urlpatterns = [
    path('', views.member_profile, name='member'),
]
