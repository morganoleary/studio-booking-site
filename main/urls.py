from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('schedule/', views.class_schedule, name='class_schedule')
]
