from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ClassDetailForm, BookingForm
from .models import Booking

# Create your views here.

def booking_page(request):
    form = BookingForm()
    return render(
        request, 
        'class_booking/booking_form.html',
            {
            "class_booking_form": form
            }
        )


def class_booking_form(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.member = request.user.userprofile
            booking.save()
            messages.success(request, 'You have successfully booked a class!')
            return redirect('member')

    else:
        form = BookingForm()
    
    return booking_page(request)


def member_profile(request):
    booked_classes = Booking.objects.filter(member=request.user.userprofile)
    return render(
        request,
        'member_profile.html',
        {
            "booked_classes": booked_classes
        }
    )