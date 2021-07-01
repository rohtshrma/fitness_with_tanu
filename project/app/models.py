from django.db import models

# Create your models here.

class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    subject=models.CharField(max_length=255)
    text=models.TextField()

    def __str__(self):
        return self.email



class Mail(models.Model):
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.email


