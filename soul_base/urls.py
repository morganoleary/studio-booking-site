"""
URL configuration for soul_base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from contact import views as contact_views
from main import views as main_views
from member import views as member_views
from class_booking import views as class_booking_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('booking/', class_booking_views.index, name='booking'),
    path('contact/', include('contact.urls'), name='contact'),
    path('member/', member_views.index, name='member'),
    path('', main_views.index, name='homepage'),
]
