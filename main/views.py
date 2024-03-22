from django.shortcuts import render

# Create your views here.


def index(request):
    """
    View to render the home page.
    **Template**
    :template: `main/index.html`
    """
    return render(request, 'main/index.html')


def class_schedule(request):
    """
    View to render the class schedule page.
    **Template**
    :template: `main/class_schedule.html`
    """
    return render(request, 'main/class_schedule.html')
