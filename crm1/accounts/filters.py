from dataclasses import fields
from pyexpat import model
from django.db import DatabaseError
import  django_filters
from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Order
        fields= '__all__'
        exclude = ['customer', 'date_created']
