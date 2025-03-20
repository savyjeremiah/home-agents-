from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib import messages


def home(request):
   
    products = Product.objects.all()  
    return render(request, 'home.html', {'products': products})

def contact(request):
    return render(request, 'contact.html')

def properties(request):
    products = Product.objects.all()  
    return render(request, 'properties.html', {'products': products})
    

def property_details(request):
    return render(request, 'property-details.html')

