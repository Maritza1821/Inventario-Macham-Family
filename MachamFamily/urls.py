"""MachamFamily URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from Inventario.views import * 

from MachamFamily.settings import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Inventario.urls')),
    path('', login_view, name="vista_login"),
    path('login/', login_view, name="vista_login"),
    path('inicio/', inicio_view, name="vista_inicio"),
    path('logout/', logout_view, name="vista_logout"), 
    path('registrar/', registro, name='registrar'),
    path('perfil/', perfil, name='perfil'),

    path('lista_categoria/', login_required(ListadoCategoria.as_view()), name ='listar_categoria'),
    path('crear_categoria/', login_required(CrearCategoria.as_view()), name = 'crear_categoria'),
    path('editar_categoria/<int:pk>/', login_required(ActualizarCategoria.as_view()), name = 'editar_categoria'),
    path('eliminar_categoria/<id>/', eliminar_categoria, name = 'eliminar_categoria'),
    
    path('lista_cliente/', login_required(ListadoCliente.as_view()), name ='listar_cliente'),
    path('crear_cliente/', login_required(CrearCliente.as_view()), name = 'crear_cliente'),
    path('editar_cliente/<int:pk>/', login_required(ActualizarCliente.as_view()), name = 'editar_cliente'),
    path('eliminar_cliente/<id>/', eliminar_cliente, name = 'eliminar_cliente'),

    path('lista_compra/', login_required(ListadoCompra.as_view()), name ='listar_compra'),
    path('crear_compra/', login_required(CrearCompra.as_view()), name = 'crear_compra'),
    path('editar_compra/<int:pk>/', login_required(ActualizarCompra.as_view()), name = 'editar_compra'),
    path('eliminar_compra/<id>/', eliminar_compra, name = 'eliminar_compra'),

    path('lista_producto/', login_required(ListadoProducto.as_view()), name ='listar_producto'),
    path('crear_producto/', login_required(CrearProducto.as_view()), name = 'crear_producto'),
    path('editar_producto/<int:pk>/', login_required(ActualizarProducto.as_view()), name = 'editar_producto'),
    path('eliminar_producto/<id>/', eliminar_producto, name = 'eliminar_producto'),
    
    path('lista_proveedor/', login_required(ListadoProveedor.as_view()), name ='listar_proveedor'),
    path('crear_proveedor/', login_required(CrearProveedor.as_view()), name = 'crear_proveedor'),
    path('editar_proveedor/<int:pk>/', login_required(ActualizarProveedor.as_view()), name = 'editar_proveedor'),
    path('eliminar_proveedor/<id>/', eliminar_proveedor, name = 'eliminar_proveedor'),
    
    path('lista_venta/', login_required(ListadoVenta.as_view()), name ='listar_venta'),
    path('crear_venta/', login_required(CrearVenta.as_view()), name = 'crear_venta'),
    path('editar_venta/<int:pk>/', login_required(ActualizarVenta.as_view()), name = 'editar_venta'),
    path('eliminar_venta/<id>/', eliminar_venta, name = 'eliminar_venta'),

    path('ajax_load_project/', ajax_load_project, name='ajax_load_project'),
    
] 

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
admin.site.site_header = 'MACHAM FAMILY MUEBLES CONFORT'
