from django.shortcuts import render

from .models import contactlist
from .models import contactform


# Create your views here.
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact_form_data = contactform(name=name,email=email,subject=subject,message=message)
        contact_form_data.save()
                
    contact_data = contactlist.objects.all()[0]
    context = {
        'my_contact':contact_data
    }
    return render(request,'contact.html',context)