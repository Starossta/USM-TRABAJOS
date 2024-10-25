from django.shortcuts import render,redirect,  get_object_or_404
from .forms import RegistroForm
from .models import Producto, Pedido, PedidoProducto
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
            return redirect('login')
    else:
        form = RegistroForm()
    data={
        'form': form
    }
    return render(request, 'core/registro.html', data)

def ver_carrito(request):
    carrito = request.session.get('carrito', {})  # Obtener el carrito como diccionario
    if isinstance(carrito, list):
        carrito = {}

    productos = Producto.objects.filter(id__in=carrito.keys())  # Obtener los productos con los IDs en el carrito
    total = 0
    carrito_items = []

    for producto in productos:
        cantidad = carrito.get(str(producto.id), 0)  # Obtener la cantidad del producto
        subtotal = producto.precio * cantidad
        total += subtotal
        carrito_items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal,
        })
    data={
        'carrito_items': carrito_items, 'total': total
    }

    return render(request, 'core/carrito.html', data)



def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    
    if str(producto_id) in carrito:
        del carrito[str(producto_id)] 
    request.session['carrito'] = carrito
    
    return redirect('ver_carrito')

def confirmar_pedido(request):
    carrito = request.session.get('carrito', {})

    # Obtener los productos del carrito
    productos_ids = carrito.keys()
    productos = Producto.objects.filter(id__in=productos_ids)

    total = 0
    productos_pedido = []

    # Calcular el total considerando la cantidad de cada producto
    for producto in productos:
        cantidad = carrito[str(producto.id)]  # Cantidad de este producto en el carrito
        total += producto.precio * cantidad
        # Añadir el producto con su cantidad al pedido
        productos_pedido.append((producto, cantidad))

    # Crear el pedido
    pedido = Pedido.objects.create(cliente=request.user, total=total)

    # Añadir productos al pedido con cantidades
    for producto, cantidad in productos_pedido:
        PedidoProducto.objects.create(pedido=pedido, producto=producto, cantidad=cantidad)

    # Vaciar el carrito despues de confirmar el pedido
    request.session['carrito'] = {}

    return redirect('ver_carrito')
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    
    # Obtener el carrito de la sesion o crear uno nuevo como diccionario
    carrito = request.session.get('carrito', {})

    if isinstance(carrito, list):
        carrito = {} 

    # Agregar el producto al carrito o incrementar su cantidad si ya está
    if str(producto_id) in carrito:
        carrito[str(producto_id)] += 1
    else:
        carrito[str(producto_id)] = 1

    # Guardar el carrito actualizado en la sesión
    request.session['carrito'] = carrito
    
    return redirect('ver_carrito')

def actualizar_carrito(request, producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST.get('cantidad'))
        carrito = request.session.get('carrito', {})
        
        if cantidad > 0:
            carrito[str(producto_id)] = cantidad  # Actualiza la cantidad del producto
        else:
            del carrito[str(producto_id)]  # Si la cantidad es 0, elimina el producto del carrito
        
        request.session['carrito'] = carrito  # Guarda los cambios en la sesión
    
    return redirect('ver_carrito')
