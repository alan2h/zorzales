from django.urls import path, include
from rest_framework import routers

from .views import PedidoCreateView

from . import helpers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'api', viewsets.PedidoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('alta', PedidoCreateView.as_view(), name='PedidoCreateView'),
    path('articulos/listado', helpers.articulo_list, name='articulo_list'),
    path('articulos/obtener', helpers.get_articulo, name='get_articulo'),
]
