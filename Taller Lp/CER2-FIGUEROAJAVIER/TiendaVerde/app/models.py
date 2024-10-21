from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    total = models.IntegerField()
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f'Pedido #{self.id} - ({self.estado})'
    
    def mostrar_productos(self):
        return ", ".join([producto.nombre for producto in self.productos.all()])

class PedidoProducto(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.producto.nombre} (x{self.cantidad})'


# Create your models here.
