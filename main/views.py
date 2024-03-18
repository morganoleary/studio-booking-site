from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def class_schedule(request):
    return render(request, 'main/class_schedule.html')