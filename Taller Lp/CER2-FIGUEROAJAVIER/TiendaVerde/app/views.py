from django.shortcuts import render,redirect,  get_object_or_404
from django.contrib.auth.models import User
from .forms import RegistroForm
from django.db import models
from .models import Producto, Pedido

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

def ver_carrito(request):
    carrito = request.session.get('carrito', [])  # Obtener el carrito de la sesión
    productos = Producto.objects.filter(id__in=carrito)  # Obtener los productos correspondientes a los IDs en el carrito
    total = sum([producto.precio for producto in productos])  # Calcular el total
    return render(request, 'core/carrito.html', {'productos': productos, 'total': total})

def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', [])
    if producto_id in carrito:
        carrito.remove(producto_id)  # Eliminar el producto del carrito
    request.session['carrito'] = carrito  # Actualizar el carrito en la sesión
    return redirect('ver_carrito')  # Redirigir al carrito actualizado

def confirmar_pedido(request):
    carrito = request.session.get('carrito', [])
    productos = Producto.objects.filter(id__in=carrito)
    total = sum([producto.precio for producto in productos])

    # Crear el pedido
    pedido = Pedido.objects.create(cliente=request.user, total=total)
    pedido.productos.set(productos)
    pedido.save()

    # Vaciar el carrito después de confirmar el pedido
    request.session['carrito'] = []

    return render(request, 'core/carrito.html', {'pedido': pedido})

def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    carrito = request.session.get('carrito', [])  # Obtener el carrito de la sesión o crear uno vacío
    carrito.append(producto.id)  # Agregar el ID del producto al carrito
    request.session['carrito'] = carrito  # Guardar el carrito en la sesión
    return redirect('ver_carrito')  # Redirigir a la vista del carrito

