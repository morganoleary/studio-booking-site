from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'phone', 'email', 'class_interested', 'message',)
