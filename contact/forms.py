from django import forms
from .models import ContactRequest, DropdownObject

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'phone', 'email', 'class_interested', 'message',)
