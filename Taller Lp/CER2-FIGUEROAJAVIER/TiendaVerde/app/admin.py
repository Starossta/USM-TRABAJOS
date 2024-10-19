from django.contrib import admin
from .models import Producto
from .models import Pedido

admin.site.register(Producto)
admin.site.register(Pedido)

# Register your models here.
