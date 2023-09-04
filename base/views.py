from django.shortcuts import render
from .models import *
from django.views.generic import  *

# Create your views here.


class HomePageView(ListView):
    model = Home
    template_name = 'pages/home.html'