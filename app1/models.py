from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


## models means table

class Employee(models.Model):

    eid = models.IntegerField(primary_key=True)
    e_name = models.CharField(max_length=50)
    e_email= models.EmailField(max_length=25)

    def __str__(self):
        return self.e_name
        # return super().__str__()

class Post(models.Model):
    title= models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author= models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})