from django import forms
from .models import ContactRequest, DropdownObject

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'phone', 'email', 'message', 'class_interested')
        
    # # Help from: https://docs.djangoproject.com/en/5.0/ref/forms/widgets/
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['class_interested'].queryset = DropdownObject.objects.all()