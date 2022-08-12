from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Submit, Row, Column, Button

from .models import Contact


class ContactForm(ModelForm):
    
    class Meta:
        model = Contact
        fields = ('name', 'email','title','message')
        widgets = {
            'title':forms.TextInput(attrs= {'placeholder':'Your message title or subject'}),  
            'message':forms.Textarea(attrs= {'placeholder':'Please drop us a message'}),    
        } 
    

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['message'].widget.attrs = {'rows':5}
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
    
        self.helper.form_show_labels = True
        
    