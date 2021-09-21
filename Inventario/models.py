from django.db import models
from django.forms.models import model_to_dict
from django.utils.safestring import mark_safe
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime
 
class Categoria(models.Model):    
    nombre = models.CharField(max_length=50) 
    estado = models.BooleanField('Estado', default=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'Categorias'
        ordering = ['id']
        
class Cliente(models.Model):
    cedula = models.CharField(max_length=10,blank=False,unique=True,null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    celular = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    estado = models.BooleanField('Estado', default=True)  
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'Clientes'
        ordering = ['id']
    
    def __str__ (self): 
        return self.nombre
        
tipo_entidad = [
    ('Propietario', 'Propietario'),
    ('Empresa', 'Empresa'),
]  
class Proveedor(models.Model): 
    cedula = models.CharField(max_length=13,blank=False,unique=True,null=False)
    nombre = models.CharField(max_length=50) 
    entidad=models.CharField(max_length=50, choices=tipo_entidad, default='available')
    direccion = models.CharField(max_length=50)
    estado = models.BooleanField('Estado', default=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores' 
        db_table = 'Proveedores'
        ordering = ['id'] 

def url_producto(self, filename):
    ruta = "media/img/Productos/%s/%s"%(self.foto_producto, str(filename))
    return ruta
class Producto(models.Model): 
    codigo = models.CharField(max_length=20,unique=True,blank=False,null=False)
    nombre = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=30)
    existencia = models.IntegerField()
    foto_producto = models.ImageField(upload_to=url_producto,blank=True)
    precio = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    fk_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, blank=False)
    fk_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=False)
    estado = models.BooleanField('Estado', default=True)
    
    def foto_producto1(self):
        return mark_safe('<a href="/media/%s" target="_blank"> <img src="/media/%s" hight="50px" width="50px"/> </a>'%(self.foto_producto, self.foto_producto))
    
    foto_producto1.allow_tags = True

    def toJSON(self):
        item = model_to_dict(self)
      
        return item

    
   
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Productos'
        ordering = ['id']

class Compra(models.Model): 
    n_compra = models.CharField(max_length=100,unique=True)
    fk_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=False)
    fk_proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(default= datetime.now)
    cantidad = models.IntegerField()
    precio = models.DecimalField(default=0.00,max_digits=8,decimal_places=2) 
    estado = models.BooleanField('Estado', default=True)
   
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        db_table = 'Compras'
        ordering = ['id']
        
class Venta(models.Model):
    n_venta = models.CharField(unique=True, max_length=100)
    fk_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=False)
    fecha = models.DateField(default= datetime.now)
    subtotal = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    iva = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    
    total = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    def __str__(self):
        return self.fk_cliente.nombre
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'Ventas' 
        ordering = ['id']

class DetalleVenta(models.Model):
    fk_producto = models.ForeignKey(Producto,on_delete=models.CASCADE,verbose_name='Producto')
    cantidad = models.IntegerField(verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    iva = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)    
    total = models.DecimalField(default=0.00,max_digits=8,decimal_places=2)
    fk_venta = models.ForeignKey(Venta,on_delete=models.CASCADE, verbose_name='Venta')

# def url_perfil(self, filename):
#     ruta = "static/img/Perfiles/%s/%s"%(self.usuario, str(filename))
#     return ruta

# class Perfil(models.Model):
#     usuario = models.OneToOneField(User, on_delete=models.CASCADE)
#     telefono = models.IntegerField()
#     direccion = models.TextField()
#     cedula = models.CharField(max_length=10)
#     foto = models.ImageField(upload_to=url_perfil)
#     estado = models.BooleanField('Estado', default=True)
        
#     def __str__(self):
#         return self.usuario.username
    
#     def foto_perfil(self):
#         return mark_safe('<a href="/%s" target="_blank"> <img src="/%s" hight="50px" width="50px"/> </a>'%(self.foto, self.foto))

#     foto_perfil.allow_tags = True
    
#     class Meta:
#         verbose_name = 'Perfil'
#         verbose_name_plural = 'Perfiles'
#         db_table = 'Perfiles' 
#         ordering = ['id']


class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return self.usuario.username

    