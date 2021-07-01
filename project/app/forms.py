from django.forms import ModelForm
from django import forms
from app.models import Feedback,Mail

class FeedbackForm(ModelForm):
    class Meta:
        model=Feedback
        fields=['name','email','subject','text']

        widgets={
            'name': forms.TextInput(attrs={'class': 'form-control', 'name': 'feedback', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'name': 'feedback', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'name': 'feedback', 'placeholder': 'Subject'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'name': 'feedback', 'placeholder': 'Message'})

        } 

class MailForm(ModelForm):
    class Meta:
        model=Mail
        fields=['email']



