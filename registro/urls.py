from django.contrib import admin
from django.urls import path
from  registro import views

urlpatterns = [
    path('verClientes/',views.listclientes),
    path('clientes/',views.verClientes),
    path('verificarcliente/',views.verificar),
    path('mantenimientocliente/',views.cliente_mantenimiento),
    path('mostrarcliente/',views.mostrarcliente),

    path('verProductos/',views.listproductos),
  
]   