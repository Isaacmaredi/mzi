from django.db import models

from datetime import date

# Create your models here.
class Launch(models.Model):
    launch_date = models.DateField()
    slider1_message = models.TextField(null=True, blank=True)
    slider2_message = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.launch_date.strftime("%Y-%m-%d") + '-' + self.slider1_message
    
    
    @property
    def days_to_launch(self):
        today = date.today()
        days_to_launch = self.launch_date - today
        days_left = str(days_to_launch).split(' ',1)[0]
        int_days_left = int(days_left)
        return int_days_left
        
        