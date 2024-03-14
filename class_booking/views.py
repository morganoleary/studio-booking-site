from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
def booking(request):

    user = request.user
    if user.is_authenticated:
        context = {'user': user, 'user.is_authenticated': True}
    else:
        context = {'user': None, 'user.is_authenticated': False}
    return render(request, 'class_booking/booking.html', context)
