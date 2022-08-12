from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Contact
from .forms import ContactForm

# Create your views here.

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    
    template_name = 'contacts/contact.html'
    
    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'Thank you for getting in touch. Your query will be addressed in due course!'
            )
        return super().form_valid(form)
    
    
    
    
# def create_contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         title= request.POST.get('title')
#         message = request.POST.get('message')
#         email = request.POST.get('email')
    
        
#         contact = Contact(name=name, title=title, message=message, email=email)
#         contact.save()
#         messages.success(request,'Thank you for your message! Our admin will conact you if necessary')
#     return render(request, 'contacts/contact.html')
        