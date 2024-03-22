from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import ClassDetail, Booking


class ClassDetailForm(forms.ModelForm):
    """
    Form for creating or updating class details.
    """
    class Meta:
        model = ClassDetail
        fields = ('class_name', 'description', 'price', 'duration', 'capacity')


class BookingForm(forms.ModelForm):
    """
    Form for making a class booking.
    """
    class Meta:
        model = Booking
        fields = ('booked_class', 'class_date', 'class_time')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['class_date'].widget = forms.widgets.DateInput(
             attrs={'type': 'date', 'class': 'form-control'})
        self.fields['class_time'].widget = forms.widgets.TimeInput(
             attrs={'type': 'time'})

    def clean(self):
        """
        Custom validation to ensure selected class date/time
        is within class availability.
        """
        cleaned_data = super().clean()
        booked_class = cleaned_data.get('booked_class')
        class_date = cleaned_data.get('class_date')
        class_time = cleaned_data.get('class_time')

        available_options = {
            'Mat Pilates for Stabilization': [
                'Monday 16:30', 'Wednesday 16:30', 'Friday 14:00'
                ],
            'Mat Pilates Flow': ['Monday 17:15', 'Wednesday 17:15'],
            'Strength and Stretch Movement Class': ['Friday 14:45']
        }

        # Get the day and time of the selected class datetime
        selected_datetime = datetime.combine(class_date, class_time)

        # Check if the selected day and time are in the allowed class times
        if selected_datetime.strftime('%A %H:%M') not in available_options[booked_class.class_name]:
            # Raise an error if date & time don't fit class availability
            raise ValidationError(
                f"Invalid class date/time for {booked_class.class_name}")

        return cleaned_data
