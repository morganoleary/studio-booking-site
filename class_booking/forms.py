from django import forms
# from django.contrib.auth.models import User
from .models import ClassDetail, Booking
# from member.models import UserProfile

# this form should only offer a dropdown for the class and autofill the description, etc.
class ClassDetailForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = ('class_name', 'description', 'price', 'duration', 'capacity')

    # # get fields from the ClassDetail model to add to the form
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['class_name'] = forms.CharField(max_length=100)
    #     self.fields['description'] = forms.TextField()
    #     self.fields['price'] = forms.DecimalField(max_digits=8, decimal_places=2)
    #     self.fields['duration'] = forms.CharField(max_length=50)
    #     self.fields['capacity'] = forms.IntegerField()


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booked_class', 'class_date', 'class_time')
