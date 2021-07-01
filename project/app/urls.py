from django.urls import path
from app.views import feedback,aboutUs,blog,contact, workshop
urlpatterns = [
   path('',feedback,name='home'),
   path('about',aboutUs,name='about'),
   path('blog', blog, name='blog'),
   path('contact',contact,name='contact'),
   path('workshops',workshop,name='workshop')

]
