from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    """
    Form for submitting contact requests.
    """
    class Meta:
        model = ContactRequest
        fields = ('name', 'phone', 'email', 'message', 'class_interested')
