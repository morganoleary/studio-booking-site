from . import views
from django.urls import path


urlpatterns = [
    path('', views.member_profile, name='member'),
]