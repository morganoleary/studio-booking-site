from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            messages.add_message(
            request, messages.SUCCESS,
            'Your message has been sent!'
        )

    else:
        form = ContactForm()

    return render(
        request,
        "contact/contact_form.html",
        {
            "contact_form": form
        }
    )