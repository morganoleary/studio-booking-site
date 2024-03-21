from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import BookingForm
from .models import Booking

# Create your views here.

def class_booking_form(request):
    """View to handle class booking form submission

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        form = BookingForm(data=request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.member = request.user.userprofile
            booking.save()
            messages.success(request, "Class booked successfully!")
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


def cancel_booking(request, booking_id):
    """
    View to cancel a booked class
    """
    booking = get_object_or_404(Booking, booking_id=booking_id)

    if booking.member.member == request.user:
        booking.delete()
        messages.success(request, "This booking has been canceled.")
        return HttpResponseRedirect(reverse('member'))
    else:
        messages.success(request, "Sorry you do not have permission to cancel this booking.")
        return redirect('member')