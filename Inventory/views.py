from django.shortcuts import render
from .forms import *
from .models import *
# Create your views here.



def Homepage(request):

    context = {
        "name": "Anu",
        "role":"manager",
        "numbers":[1,2,3,4,5],
        "marks":{
            "tamil":100,
            "English":99
        }
    }
    return render(request, 'home.html', context)

def AboutPage(request):
    return render(request, 'about.html')

def ContactPage(request):
    return render(request, 'contact.html')

def ServicePage(request):
    return render(request, 'services.html')        

def ProductsAdd(request):
    context ={
      'product_form':Product_Form()
    }

    if request.method == "POST":
       product_form = Product_Form(request.POST)

       if product_form.is_valid():
          product_form.save()

    return render(request, 'products.html', context)