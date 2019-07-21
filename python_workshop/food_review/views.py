from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant,Restaurant_Review,Review_Detail
# Create your views here.

def home(response):
    queryset = Restaurant.objects.all()
    context = {
        "objectList": queryset
    }
    return render(response,'home.html',context)

# def review(response, id):
#     ls = Restaurant.objects.get(id=)
# def create(response):
#     if response.method == "POST":
#         form = CreateNewList(response.POST)

#         if form.is_valid():
#             n = form.cleaned_data["name"]
#             response.user.