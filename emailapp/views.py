from django.shortcuts import render
from emailproj.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

# Create your views here.


def home(request):
    sub = forms.Emailform()

    if request.method == 'POST':
        sub = forms.Emailform(request.POST)
        subject = "Welcome To Project"
        message = "Hope u r enjoying this project"
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER,
                  [recepient], fail_silently=False)
        return render(request, 'emailapp/success.html', {'recepient': recepient})

    return render(request, 'emailapp/index.html', {'form': sub})
