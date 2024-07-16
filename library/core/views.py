
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader



# Create your views here.

def home_page(request):
    return render(request,'pages/home.html')

def about_page(request):
    return render(request, 'pages/about.html')


