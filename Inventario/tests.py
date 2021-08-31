from django.test import TestCase
from Inventario.models import *

# Listar Categoria 
print(Categoria.objects.all())

for i in Categoria.objects.filter(): 
    print (id)
