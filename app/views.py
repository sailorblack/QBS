from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'app/index.html')
def about(request):
    return render(request, 'app/about.html')

def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():#ensuring the form filled by user is correct
            subject = "Website Inquiry" 
            body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
            message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return render (request, "app/index.html")

    form = ContactForm()#calling form from forms.py 
    return render(request, "app/contact.html", {'form':form})