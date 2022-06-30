from cmath import phase
import email
from pydoc import describe
from sre_constants import CATEGORY
from sre_parse import CATEGORIES
from statistics import mode
from tkinter.messagebox import NO
from tokenize import blank_re
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name=models.CharField(max_length=200,null=True)
    location=models.CharField(max_length=200,null=True)
    employer=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    title=models.CharField(max_length=200,null=True)
    TYPE=(
        ('MENTOR','Mentor'),
        ('MEMBER','Member'),
    )
    type=models.CharField(max_length=20,choices=TYPE,default=None,blank=True,null=True)
    expertis=models.CharField(max_length=200,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.user)



#class Product(models.Model):
#    CATEGORY=(
#        ('Indoor','Indoor'),
#        ('Out Door','Out Door'),
#    )
#    name=models.CharField(max_length=200,null=True)
#    price=models.FloatField(null=True)
#    category=models.CharField(max_length=200,null=True,choices=CATEGORY)
#    description=models.CharField(max_length=200,null=True,blank=True)
#    date_created=models.DateTimeField(auto_now_add=True)
    


class Order(models.Model):
    STATUS=(
        ('MentorP','MentorP'),
        ('MentorA','MentorA'),
        ('MemberA','MemberA'),
        ('MemberP','MemberP'),
        
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
  
    #product=models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    #date_created=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    
    def __str__(self):
        return self.status


