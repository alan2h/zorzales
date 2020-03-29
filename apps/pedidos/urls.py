from django.urls import path, include
from rest_framework import routers

from .views import PedidoCreateView, PedidoListView

from . import helpers
from . import viewsets

router = routers.DefaultRouter()
router.register(r'api', viewsets.PedidoViewSet)
router.register(r'articulos/api', viewsets.PedidoArticuloViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('alta', PedidoCreateView.as_view(), name='PedidoCreateView'),
    path('listado', PedidoListView.as_view(), name='PedidoListView'),
    path('articulos/listado', helpers.articulo_list, name='articulo_list'),
    path('articulos/obtener', helpers.get_articulo, name='get_articulo'),
]
