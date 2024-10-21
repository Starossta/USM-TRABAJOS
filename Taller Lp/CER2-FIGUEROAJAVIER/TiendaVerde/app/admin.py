from django.contrib import admin
from .models import Producto
from .models import PedidoProducto, Pedido
from django.contrib.auth.models import Group, Permission



vendedores_group, created = Group.objects.get_or_create(name='Vendedores')
permisos_pedidos = Permission.objects.filter(codename__in=['view_pedido', 'change_pedido','PedidoAdmin'])
vendedores_group.permissions.add(*permisos_pedidos)

class PedidoProductoInline(admin.TabularInline):
    model = PedidoProducto
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id',  'estado']
    list_filter = ['estado']
    search_fields = ['vendedor__username', 'pedidoproducto__producto__nombre']
    inlines = [PedidoProductoInline] 


admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Producto)


# Register your models here.
