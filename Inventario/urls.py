from rest_framework import routers
from .viewset import *


router = routers.SimpleRouter()
router.register('api/categoria',CategoriaViewset)
router.register('api/login',LoginViewSet)
router.register('api/cliente',ClienteViewset)
router.register('api/proveedor',ProveedorViewset)
router.register('api/producto',ProductoViewset)
router.register('api/compra',CompraViewset)
router.register('api/venta',VentaViewset)
router.register('api/detallesventa',DetallesViewset)
router.register('api/detallesventaalter',DetallesViewsetAlter)


urlpatterns = router.urls