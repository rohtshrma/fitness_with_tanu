from django.shortcuts import render
from app.models import Feedback,Mail
from app.forms import FeedbackForm,MailForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib import messages
from project.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

# Create your views here.

def selfEmail(request):
    email = 'fitnesswithtanu@gmail.com'
    subject = request.POST['subject']
    message = 'Form ' + request.POST['email']+ '                 ' + request.POST['text']
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)

def userEmail(request):
    email = request.POST['email']
    subject = request.POST['subject']
    message = request.POST['text']
    recepient = email
    send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)


def feedback(request):
    if request.method=='POST':
            form=FeedbackForm(request.POST)
            if form.is_valid():
                selfEmail(request)
                form.save()
                return HttpResponseRedirect(reverse('home'))
            mailform = MailForm(request.POST)
            if mailform.is_valid():
                mailform.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form=FeedbackForm()
        mailform=MailForm()
        return render(request,'index.html', { 'mailform':mailform} )

def aboutUs(request):
    if request.method == 'POST':
        mailform = MailForm(request.POST)
        if mailform.is_valid():
            mailform.save()       
    mailform = MailForm()
    return render(request, 'about.html', {'mailform': mailform})


def blog(request):
    if request.method == 'POST':
        mailform = MailForm(request.POST)
        if mailform.is_valid():
            mailform.save()
    mailform = MailForm()
    return render(request, 'blog.html', {'mailform': mailform})
    



def contact(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            selfEmail(request)
            form.save()
            return HttpResponseRedirect(reverse('home'))
        mailform = MailForm(request.POST)
        if mailform.is_valid():
            mailform.save()
        return HttpResponseRedirect(reverse('home'))
    else:
        form=FeedbackForm()
        mailform=MailForm()
        return render(request,'contact.html', {'form':form, 'mailform':mailform} )


def workshop(request):
    if request.method == 'POST':
        mailform = MailForm(request.POST)
        if mailform.is_valid():
            mailform.save()
    mailform = MailForm()
    return render(request, 'workshop.html', {'mailform': mailform})



