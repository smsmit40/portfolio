from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
import os

def index(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        return render(request, 'app/index.html', {'projects': projects})

    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            receiver = ['seansrestaurantcontact@gmail.com']

            try:
                send_mail(subject, message, email, receiver)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            projects = Project.objects.all()
            return render(request, 'app/index.html', {'projects': projects})
