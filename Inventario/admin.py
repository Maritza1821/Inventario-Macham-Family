from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class  CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin):
    list_display = ('nombre','estado')
    search_fields = ['nombre']
    resource_class = CategoriaResource

class  ClienteResource(resources.ModelResource):
    class Meta:
        model = Cliente

class ClienteAdmin(ImportExportModelAdmin):
    list_display = ('nombre','cedula','apellido','direccion','celular','estado', 'email')
    search_fields = ['nombre','cedula']
    resource_class = ClienteResource
 
class  ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor

class ProveedorAdmin(ImportExportModelAdmin):
    list_display = ( 'cedula','nombre','entidad','direccion','estado')
    search_fields = ['nombre']
    resource_class = ProveedorResource
   
class  ProductoResource(resources.ModelResource):
    class Meta:
        model = Producto

class ProductoAdmin(ImportExportModelAdmin):
    list_display = ("id",'codigo','nombre','descripcion','existencia','foto_producto','precio','fk_categoria','fk_proveedor','estado')
    search_fields = ['nombre','codigo']
    resource_class = ProductoResource
class  CompraResource(resources.ModelResource):
    class Meta:
        model = Compra

class CompraAdmin(ImportExportModelAdmin):
    list_display = ('n_compra','fk_producto','fk_proveedor','fecha','cantidad','precio','estado')
    search_fields = ['n_compra']
    resource_class = CompraResource

class  VentaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class  DetalleResource(resources.ModelResource):
    class Meta:
        model = DetalleVenta
class DetallesAdmin(ImportExportModelAdmin):
    list_display = ('fk_producto','cantidad','subtotal','iva','total','fk_venta')
    search_fields = ['fk_producto']
    resource_class = VentaResource




class VentaAdmin(ImportExportModelAdmin):
    list_display = ('n_venta','fk_cliente','fecha','subtotal','iva','total')
    search_fields = ['n_venta']
    resource_class = VentaResource

# class PerfilResource(resources.ModelResource):
#     class Meta:
#         model = Perfil

# class PerfilAdmin(ImportExportModelAdmin):
#     list_display = ('cedula', 'usuario', 'telefono', 'direccion', 'foto_perfil', 'estado')
#     search_fields = ['cedula', 'usuario']
#     resource_class = PerfilResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Compra,CompraAdmin)
admin.site.register(Venta,VentaAdmin)
admin.site.register(DetalleVenta,DetallesAdmin)
""" admin.site.register(Perfil,PerfilAdmin) """