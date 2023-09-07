from django.shortcuts import render

from .models import about
from .models import slider
from .models import client
# Create your views here.

def home(request):

    about_data = about.objects.all()
    slider_data = slider.objects.all()
    client_data = client.objects.all()

    my_about = {
        "about":about_data,
        "slider" : slider_data,
        "client" : client_data,
    }
    
    return render(request,'index.html',my_about)

def about_page(request):
    return render(request,'about.html')


