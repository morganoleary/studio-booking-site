from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import UserProfileForm

from class_booking.models import Booking

# Create your views here.


def member_profile(request):
    """
    View to display the profile of a logged in user.
    Displays an individual instance of
        :model: `UserProfile` and :model: `Booking`
    **Context**
    ``booked_classes``
        An instance of the :model: `Booking`
    ``user_profile``
        An instance of the :model: `UserProfile`
    ``form``
        An instance of the :form: `member.UserProfileForm`
    **Template**
    :template: `member/member_profile.html`
    """

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(member=request.user)
        booked_classes = Booking.objects.filter(member=user_profile)

        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('member')
        else:
            form = UserProfileForm(instance=user_profile)

        context = {
            'booked_classes':booked_classes,
            'user_profile': user_profile,
            'form': form
                    }
        return render(request, "member/member_profile.html", context)
    else:
        return redirect('login')
