from django.shortcuts import render
from django.http import HttpResponse
from .models import Carrera

# Create your views here.
def home(request):
    titulo = 'inicio'
    data ={
        'titulo':titulo
    }
    #mensaje="gallardo chupalo"
    #return HttpResponse(mensaje)
    return render(request,'index.html',data)
def carreras(request):
    titulo = 'carreras'
    carreras = Carrera.objects.all()
    data={
        'titulo' :titulo,
        'carreras':carreras
    }
    return render(request,'carreras.html',data)