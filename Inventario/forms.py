from django import forms
from django.forms.models import inlineformset_factory
from.models  import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username','password']
    
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
        labels = {
            'nombre' : 'Ingrese el nombre de la Categoria',         
        }
        widgets = {
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            )
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','last_name','email','password1','password2']
        labels = {
            'username' : 'Nombre',
            'last_name':'Apellido',
            'email' : 'Correo',
            'password1' : 'Contraseña',
            'password2' : 'Confirmar contraseña',
        }
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '' }),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder': '' }),
            'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder': ''}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':''}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}),
        }

class ClientesForm(forms.ModelForm):
    class Meta:
        
        model = Cliente
        fields = ['cedula','nombre','apellido','direccion','celular', 'email']
        labels = {
            'cedula' : 'Ingrese el número de cédula', 
            'nombre' : 'Ingrese el nombre del cliente',  
            'apellido' : 'Ingrese el apellido del cliente',  
            'direccion' : 'Ingrese la dirección del cliente',  
            'celular' : 'Ingrese el número de celular del cliente',   
            'email' : 'Ingresar su correo',
        }
        widgets = {
            'cedula' : forms.TextInput(
                attrs = {
                    "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Cedula',
                    'id' : 'cedula'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'apellido' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Apellido',
                    'id' : 'apellido'
                }
             ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Direccion',
                    'id' : 'direccion'
                }
            ),
            'celular' : forms.TextInput(
                attrs = {
                        "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Celular',
                    'id' : 'celular'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '' 
                }
            ),
           
           

        }  
        
class ClienteUpdaForm(forms.ModelForm):
    
    class Meta:
        model = Cliente
        fields = ['cedula','nombre','apellido','direccion','celular','email']
        labels = {
            'cedula' : 'Ingrese el número de cédula', 
            'nombre' : 'Ingrese el nombre del cliente',  
            'apellido' : 'Ingrese el apellido del cliente',  
            'direccion' : 'Ingrese la dirección del cliente',  
            'celular' : 'Ingrese el número de celular del cliente',   
            'email' : 'Ingresar su correo',
  
        }
        widgets = {
            'cedula' : forms.TextInput(
                attrs = {
                       "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Cedula',
                    'id' : 'cedula'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'apellido' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Apellido',
                    'id' : 'apellido'
                }
             ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Direccion',
                    'id' : 'direccion'
                }
            ),
            'celular' : forms.TextInput(
                attrs = {
                        "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Celular',
                    'id' : 'celular'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '' 
                }
            )

        }    

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula','nombre','apellido','direccion','celular', 'email']
        labels = {
            'cedula' : 'Ingrese el número de cédula', 
            'nombre' : 'Ingrese el nombre del cliente',  
            'apellido' : 'Ingrese el apellido del cliente',  
            'direccion' : 'Ingrese la dirección del cliente',  
            'celular' : 'Ingrese el número de celular del cliente',   
            'email' : 'Ingresar su correo',
           
        }
        widgets = {
            'cedula' : forms.TextInput(
                attrs = {
                       "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Cedula',
                    'id' : 'cedula'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'apellido' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Apellido',
                    'id' : 'apellido'
                }
             ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Direccion',
                    'id' : 'direccion'
                }
            ),
            'celular' : forms.TextInput(
                attrs = {
                        "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Celular',
                    'id' : 'celular'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '' 
                }
            ),
         
           

        }
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cedula','nombre','apellido','direccion','celular','email']
        labels = {
            'cedula' : 'Ingrese el número de cédula', 
            'nombre' : 'Ingrese el nombre del cliente',  
            'apellido' : 'Ingrese el apellido del cliente',  
            'direccion' : 'Ingrese la dirección del cliente',  
            'celular' : 'Ingrese el número de celular del cliente',   
            'email' : 'Ingresar su correo',
  
        }
        widgets = {
            'cedula' : forms.TextInput(
                attrs = {
                       "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Cedula',
                    'id' : 'cedula'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'apellido' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Apellido',
                    'id' : 'apellido'
                }
             ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Direccion',
                    'id' : 'direccion'
                }
            ),
            'celular' : forms.TextInput(
                attrs = {
                        "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Celular',
                    'id' : 'celular'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': '' 
                }
            )

        }    
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['cedula','nombre','entidad','direccion']
        labels = {
            'cedula' : 'Ingrese el número de cédula o Ruc', 
            'nombre' : 'Ingrese el nombre del Proveedor',  
            'entidad' : 'Ingrese la Entidad',  
            'direccion' : 'Ingrese la dirección del proveedor',        
        }
        widgets = {
            'cedula' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Cedula',
                    'id' : 'cedula'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'entidad' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Entidad',
                    'id' : 'entidad'
                }
             ),
            'direccion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Direccion',
                    'id' : 'direccion'
                }
            ),

        }
class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = ['codigo','nombre','descripcion','existencia','foto_producto','precio','fk_categoria','fk_proveedor']
        labels = {
            'codigo' : 'Ingrese el codigo del producto', 
            'nombre' : 'Ingrese el nombre del Producto',  
            'descrpcion' : 'Ingrese el la descripccion del producto',  
            'existencia' : 'Ingrese la cantidad e productos',    
            'foto_producto' : 'Suba la foto',    

            'precio' : 'Ingrese el precio del producto', 
            'fk_categoria' : 'Eliga la categoria del producto',   
            'fk_proveedor' : 'Eliga el proveedor del producto',     
        }
        widgets = {
            'codigo' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Codigo',
                    'id' : 'codigo'
                }
            ),
            'nombre' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Nombre',
                    'id' : 'nombre'
                }
            ),
            'descripcion' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Descripcion',
                    'id' : 'descripcion'
                }
             ),
            'existencia' : forms.TextInput(
                attrs = {
                    "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Existencia',
                    'id' : 'existencia'
                }
            ),
            'foto_producto' : forms.FileInput(
                attrs = {
                    "type":"file",
                    'class' : 'form-control',
                    'placeholder' : 'Existencia',
                    'id' : 'existencia'
                }
            ),

              'precio' : forms.TextInput(
                attrs = {
                    "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Precio',
                    'id' : 'precio'
                }
            ),
            'fk_categoria' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Categoria',
                    'id' : 'fk_categoria'
                }
             ),
            'fk_proveedor' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Proveedor',
                    'id' : 'fk_proveedor'
                }
            )
                       
        }
class CompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['n_compra','fk_producto','fk_proveedor','fecha','cantidad','precio']
        labels = {
            'n_compra' : 'Ingrese el numero de compra', 
            'fk_producto' : 'Ingrese el producto',  
            'fk_proveedor' : 'Ingrese el proveedor',  
            'fecha' : 'Ingrese la fecha de compra',  
            'cantidad' : 'Ingrese el número de productos', 
            'precio' : 'Ingrese el precio',      
        }
        widgets = {
            'n_compra' : forms.TextInput(
                attrs = {
                     "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Compra Nro',
                    'id' : 'compra'
                }
            ),
            'fk_producto' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Producto',
                    'id' : 'fk_producto'
                }
            ),
            'fk_proveedor' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Proveedor',
                    'id' : 'fk_proveedor'
                }
             ),
            'fecha' :  forms.DateInput(attrs={'type': 'date','class': 'form-control'}, format="%Y-%m-%d"),
            'cantidad' : forms.TextInput(
                attrs = {
                       "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'cantidad',
                    'id' : 'cantidad'
                }
            ),
            'precio' : forms.TextInput(
                attrs = {
                       "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Precio ',
                    'id' : 'precio'
                }
            )
        }
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['n_venta','fk_cliente','fecha','subtotal','iva','total']
        labels = {
            'n_venta' : 'Ingrese el numero de venta', 
            'fk_cliente' : 'Ingrese el cliente',  
            'fecha' : 'Ingrese la fecha de venta',  
            'subtotal' : 'SUBTOTAL',  
            'iva' : 'IVA', 
            'total' : 'TOTAL',      
        }
        widgets = {
            'n_venta' : forms.TextInput(
                attrs = {
                    "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Venta Nro',
                    'id' : 'n_venta'
                }
            ),
            'fk_cliente' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Cliente',
                    'id' : 'fk_cliente'
                }
            ),
             'fecha' :  forms.DateInput(attrs={'type': 'date','class': 'form-control'}, format="%Y-%m-%d"),
            'subtotal' : forms.TextInput(
                attrs = {
                    
                    'class' : 'form-control',
                    'placeholder' : 'Subtotal',
                    'id' : 'subtotal'
                }
            ),
            'iva' : forms.TextInput(
                attrs = {
                     
                    'class' : 'form-control',
                    'placeholder' : 'IVA',
                    'id' : 'iva'
                }
            ),
            'total' : forms.TextInput(
                attrs = {
                     
                    'class' : 'form-control',
                    'placeholder' : 'Total ',
                    'id' : 'total'
                }
            )
        }

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['fk_producto','cantidad','subtotal','iva','total','fk_venta']
        labels = {
            'fk_producto' : 'Ingrese el numero de venta', 
            'cantidad' : 'Ingrese el cliente',  
            'subtotal' : 'Ingrese la fecha de venta',  
            'iva' : 'Ingrese el subtotal',  
            'total' : 'Ingrese el número de productos', 
            'fk_venta' : 'Ingrese el valor total',      
        }
        widgets = {
            'fk_producto' : forms.Select(
                attrs = {
                    'class' : 'form-control',
                    'placeholder' : 'Producto',
                    'id' : 'fk_producto'
                }
            ),
            'cantidad' : forms.Select(
                attrs = {
                
                    'class' : 'form-control',
                    'placeholder' : 'Cantidad',
                    'id' : 'cantidad'
                }
            ),
             'subtotal' :   forms.TextInput(
                attrs = {
                      "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Subtotal',
                    'id' : 'subtotal'
                }
            ),
            'iva' : forms.TextInput(
                attrs = {
                      "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Iva',
                    'id' : 'iva'
                }
            ),
            'total' : forms.TextInput(
                attrs = {
                      "type":"number",
                    'class' : 'form-control',
                    'placeholder' : 'Total',
                    'id' : 'total'
                }
            ),
            'fk_venta' : forms.Select(
                attrs = {
                  
                    'class' : 'form-control',
                    'placeholder' : 'Venta',
                    'id' : 'Venta'
                }
            )
        }
