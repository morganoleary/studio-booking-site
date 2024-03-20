from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BookingForm

# Create your views here.


def class_booking_form(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.member = request.user.userprofile
            booking.save()
            messages.add_message(
                request,messages.SUCCESS,
                'You have successfully booked a class!'
            )
            return redirect('member')

    else:
        form = BookingForm()
    
    return render(
        request, 
        'class_booking/booking_form.html',
            {
            "class_booking_form": form
            }
        )