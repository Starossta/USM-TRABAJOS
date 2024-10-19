from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegistroForm

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

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encripta la contraseña
            user.save()
            return redirect('login')  # Redirige a la página de inicio de sesión
    else:
        form = RegistroForm()
    return render(request, 'core/registro.html', {'form': form})
