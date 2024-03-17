from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.
def member_profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(member=request.user)
        if request.method == 'POST':
            form = UserProfileForm(request.POST, instance=user_profile)
            if form.is_valid():
                form.save()
                return redirect('member')
        else:
            form = UserProfileForm(instance=user_profile)
        return render(request, "member/member_profile.html", {'user_profile': user_profile, 'form': form})
    else:
        return redirect('login')