from django import forms
# from django.contrib.auth.models import User
from .models import ClassDetail, Booking
# from member.models import UserProfile

# this form should only offer a dropdown for the class and autofill the description, etc.
class ClassDetailForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = ('class_name', 'description', 'price', 'duration', 'capacity')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booked_class', 'class_date', 'class_time')

        # AUTOFILL THE USER
        # model = UserProfile
        # fields = ('member')
