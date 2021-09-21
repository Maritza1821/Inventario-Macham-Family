
from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework.authtoken.views import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import AbstractUser, User
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from rest_framework import mixins, status, viewsets
class LoginViewSet(viewsets.GenericViewSet,generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class =UserLoginSerializer
    
    def get_permissions(self):
        print(self.action)
        permissions = [AllowAny]
       
        return [p() for p in permissions]

    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""
        print(request.data)
        serializer = UserLoginSerializer(data=request.data)       
        is_valid = serializer.is_valid()               
        if(is_valid):
            user, token = serializer.save()
            user = UserSerializer(user).data 
            data = {
                    'user': user,
                    'access_token': token
                }           
        else:
            data = {
                'error': '',
                'message': 'Usuario o contraseña incorrecto'
            }
            return Response(data, status=status.HTTP_401_UNAUTHORIZED)

        return Response(data, status=status.HTTP_201_CREATED)
from rest_framework import generics

class CategoriaViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    

class CategoriaViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ClienteViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Cliente.objects.all()
        id = self.request.query_params.get('id')
        cedula = self.request.query_params.get('cedula')
        
        if id is not None:
            queryset = queryset.filter(id=id)
            return queryset
        if cedula is not None:
            queryset = queryset.filter(cedula=cedula)
            return queryset
        return queryset

    def create(self, request, *args, **kwargs):  
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user=User.objects.create_user(username=request.data["cedula"],password=request.data["cedula"],last_name="cliente")
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ProveedorViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorSerializer



class ProductoViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
  

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Producto.objects.all()
        nombre = self.request.query_params.get('nombre')
        print(nombre)
        if nombre is not None:
            queryset = queryset.filter(nombre__icontains=nombre)
            return queryset
        return queryset

class CompraViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

    def create(self, request, *args, **kwargs):  
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        producto_id=request.data["fk_producto"]
        cantidad=request.data["fk_producto"]
        producto=Producto.objects.get(id=producto_id)
        producto.existencia=int(producto.existencia)+int(cantidad)
        producto.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

  

class VentaViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Venta.objects.all()
        n_venta = self.request.query_params.get('n_venta')
        if n_venta is not None:
            queryset = queryset.filter(n_venta=n_venta)
            return queryset
        return queryset

class DetallesViewset(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetallesSerializerA

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = DetalleVenta.objects.all()
        fk_venta = self.request.query_params.get('fk_venta')
       
        if fk_venta is not None:
            queryset = queryset.filter(fk_venta=fk_venta)
            return queryset
        return queryset

    def create(self, request, *args, **kwargs):
      
        for row in request.data:  
            serializer = self.get_serializer(data=row)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            id_producto=row["fk_producto"]
            cantidad_producto=row["cantidad"]
            producto=Producto.objects.get(id=id_producto)
            producto.existencia=int(producto.existencia)-int(cantidad_producto)
            producto.save()
        headers = self.get_success_headers(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)

class DetallesViewsetAlter(viewsets.ModelViewSet,generics.ListAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetallesSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = DetalleVenta.objects.all()
        fk_venta = self.request.query_params.get('fk_venta')
      
        if fk_venta is not None:
            queryset = queryset.filter(fk_venta=fk_venta)
            return queryset
        return queryset

    def create(self, request, *args, **kwargs):      
        for row in request.data:       
            serializer = self.get_serializer(data=row)
            serializer.is_valid(raise_exception=True)          
            self.perform_create(serializer)
        headers = self.get_success_headers(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED, headers=headers)



""" 
class PerfilViewset(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class =  PerfilSerializer """