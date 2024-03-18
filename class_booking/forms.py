from django import forms
from .models import ClassDetail, Booking


class ClassDetailForm(forms.ModelForm):
    class Meta:
        model = ClassDetail
        fields = ('class_name', 'description', 'price', 'duration', 'capacity')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('booked_class', 'class_date', 'class_time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_date'].widget = forms.widgets.DateInput(
             attrs={'type': 'date', 'class': 'form-control'})
        self.fields['class_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})
