from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='homepage'),
    path('schedule/', views.class_schedule, name='class_schedule')
]