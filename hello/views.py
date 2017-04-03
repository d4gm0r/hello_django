from django.shortcuts import render
from django.http import HttpResponse
import time

def index(request):
    return HttpResponse("Hello Django World!! You're here at: " + time.strftime("%c"))

# Create your views here.