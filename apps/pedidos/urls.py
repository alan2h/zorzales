from django.urls import path

from .views import PedidoCreateView

from . import helpers

urlpatterns = [
    path('alta', PedidoCreateView.as_view(), name='PedidoCreateView'),
    path('articulos/listado', helpers.articulo_list, name='articulo_list'),
    path('articulos/obtener', helpers.get_articulo, name='get_articulo'),
]
