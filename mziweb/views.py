import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime, date
from django.views.generic import TemplateView, ListView
from contacts.models import Contact
from .models import Launch

class HomeView(ListView):
    model = Launch
    template_name = 'mziweb/index.html'
    context_object_name = 'launches'
    
class AboutView(TemplateView):
    template_name = 'mziweb/about.html'
    
class AuthorView(TemplateView):
    template_name = 'mziweb/author.html'
    model = Contact
    
    def get_message(request, *args, **kwargs):
        contact = Contact()
        if request.method == 'POST':
            message = request.POST.get('message')
            name =request.POST.get('name')
            title = request.Post.get('title')
            email = request.Post.get('email')
            contact = Contact(name=name, email=email, title=title,message=message)
            contact.save()
            message.success = (request, 'Thank you for making contact. We will get back to you soon')
            print('Posted is done ')
            return redirect('mziweb:author')
            
    
class MyBookView(TemplateView):
    template_name = 'mziweb/mybook.html'
    





