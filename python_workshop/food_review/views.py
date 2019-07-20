from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant
# Create your views here.

def home(response):
    restaurant = Restaurant()
    return render(response,'home.html',{'Restaurant':restaurant})