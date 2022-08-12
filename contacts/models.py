from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name + ' - ' + self.title
    
    def get_absolute_url(self):
        return reverse('mziweb:home')
    
    
    
    