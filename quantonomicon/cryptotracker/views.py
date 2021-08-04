from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'cryptotracker/home.html')


def about(request):
    return HttpResponse('<h1> About quantonomicon cryptotracker </h1>')

# Create your views here.
