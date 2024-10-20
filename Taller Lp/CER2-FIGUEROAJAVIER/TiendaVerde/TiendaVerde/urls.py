"""
URL configuration for TiendaVerde project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home, productos, formulario, registro, confirmar_pedido, ver_carrito, eliminar_del_carrito, agregar_al_carrito

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path('productos/', productos, name='productos'),
    path('formulario/', formulario, name='formulario'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('registro/', registro, name='registro'),
    path('agregar-al-carrito/<int:producto_id>/', agregar_al_carrito, name='agregar_al_carrito'),
    path('ver-carrito/', ver_carrito, name='ver_carrito'),
    path('eliminar-del-carrito/<int:producto_id>/', eliminar_del_carrito, name='eliminar_del_carrito'),
    path('confirmar-pedido/', confirmar_pedido, name='confirmar_pedido'),
]
