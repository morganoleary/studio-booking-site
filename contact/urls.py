from . import views
from django.urls import path

urlpatterns = [
    path('', views.contact_form, name='contact')
]