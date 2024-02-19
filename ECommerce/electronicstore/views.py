from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, 'electronicstore/index.html')


def about(request):
    return render(request, 'electronicstore/about.html')