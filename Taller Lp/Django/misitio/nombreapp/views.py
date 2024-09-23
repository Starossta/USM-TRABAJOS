from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    mensaje="gallardo chupalo"
    return HttpResponse(mensaje)