from operator import truediv
from django.db import models

# Create your models here.
class MessegeDb(models.Model):
    name=models.CharField(max_length=200,null=True,blank=False)
    email=models.CharField(max_length=200,null=True,blank=False)
    subject=models.CharField(max_length=200,null=True,blank=False)
    message=models.CharField(max_length=200,null=True,blank=False)