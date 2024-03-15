from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ClassDetailForm, BookingForm

# Create your views here.

def booking_page(request):
    return render(
        request, 
        'class_booking/booking.html',
        )
# use return booking_page(request) when needing to render booking.html file in other functions:


def class_booking_form(request):
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.instance.member = request.user.userprofile
            form.save()
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

# booking page from menu
## if user is authenticated (logged in) >> booking page (booking.html)

### book a class >> inserts user info (hello user!), provides dates & times available (choices), with submit btn
### class choices = class, date, time (need to add date & time choices to Booking model???)
### when submitted >> capacity is updated, booking sent to admin site, success message of booking (w/ details), redirect to user profile (member_profile.html) w/ updated class list

## if user is NOT authenticated >> sign in page w/ option to sign up (if not done already)

### ((sign in page >>> should redirect user to booking page? home page?))