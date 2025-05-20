from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Homepage),
    path('about/', AboutPage),
    path('contact/', ContactPage),
    path('service/', ServicePage),
    path('product/add/', ProductsAdd),
    
]
