from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('__all__')


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        '''Check credentials.'''
        print(data)
        user = authenticate(
            username=data['username'], password=data['password'])

        if user is not None:
            self.context['user'] = user
            return data
        else:
            raise serializers.ValidationError('Invalid credentials')

        

    def create(self, data):
        '''Generate or retrieve new token.'''
        print("askfnakj")
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key

    def update(self, instance, validated_data):

        return instance


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'
class ProductoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Producto
        fields = ("id","codigo","nombre","descripcion","existencia","precio","fk_categoria","fk_proveedor","estado")

from rest_framework.renderers import JSONRenderer
class CompraSerializer(serializers.ModelSerializer):
        

    class Meta:
        model = Compra
        fields = ("id","n_compra","fk_producto","fk_proveedor","fecha","cantidad","precio","estado")

    
    def validate(self, data):
        print(data)
        """
        Check that the blog post is about Django.
        """
       
        return data

    
        
class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = '__all__'

          
class DetallesSerializerA(serializers.ModelSerializer):
   
    class Meta:
        model = DetalleVenta
        fields = '__all__'
          
class DetallesSerializer(serializers.ModelSerializer):
    fk_producto = serializers.StringRelatedField()
    class Meta:
        model = DetalleVenta
        fields = '__all__'
# class PerfilSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Perfil
#         fields = '__all__'