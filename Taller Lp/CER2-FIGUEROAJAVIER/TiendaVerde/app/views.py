from django.shortcuts import render

# Create your views here.
def home(request):
    titulo='Inicio'
    data ={
        'titulo':titulo
    }
    return render(request,'core/index.html',data)

def productos(request):
    titulo='Productos'
    data ={
        'titulo':titulo
    }
    return render(request, 'core/productos.html',data)
def formulario(request):
    titulo='Formulario'
    data={
        'titulo':titulo
    }
    return render(request, 'core/formulario.html', data)
