from django.contrib import admin
from .models import Producto
from .models import Pedido
from django.contrib.auth.models import Group, Permission



vendedores_group, created = Group.objects.get_or_create(name='Vendedores')
permisos_pedidos = Permission.objects.filter(codename__in=['view_pedido', 'change_pedido'])
vendedores_group.permissions.add(*permisos_pedidos)


admin.site.register(Producto)
admin.site.register(Pedido)

# Register your models here.
