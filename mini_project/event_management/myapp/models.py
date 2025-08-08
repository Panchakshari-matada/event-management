from django.db import models

# Create your models here.

class Register(models.Model):
    name = models.CharField(max_length=255)  
    email = models.EmailField(unique=True)  
    usn = models.CharField(max_length=20, unique=True)  
    branch = models.CharField(max_length=100)  
    sem = models.IntegerField() 
    phone_number = models.CharField(max_length=15)  

    def _str_(self):
        return self.name


class AddEvent(models.Model):
    event_id = models.AutoField(primary_key=True)  
    event_title = models.CharField(max_length=255) 
    category = models.CharField(max_length=100) 
    branch = models.CharField(max_length=20) 
    description = models.TextField()  
    venue = models.CharField(max_length=255)  
    timing = models.DateTimeField()  
    name_of_coordinator = models.CharField(max_length=255)  
    phone_number = models.CharField(max_length=15)  
    upload_poster = models.ImageField(upload_to='event_posters/', null=True, blank=True) 


    def _str_(self):
        return self.event_title