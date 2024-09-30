from django.shortcuts import render
from django.http import HttpResponse

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
    carreras=('Tecnico en informatica',
    'Ingenieria en informatica','ing civil informatica')
    data={
        'titulo' :titulo,
        'carreras':carreras
    }
    return render(request,'carreras.html',data)