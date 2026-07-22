from django.shortcuts import render
from django.http import *
# Create your views here.
def Index(request):
    return render(request, 'index.html')