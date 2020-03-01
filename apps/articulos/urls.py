from django.urls import path, include

from .views import ArticuloCreateView, ArticuloListView, \
    ArticuloUpdateView, ArticuloDeleteView, ArticuloDetailView, ArticuloReportePDF
from .viewset import ArticuloViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', ArticuloViewSet)

# ajax functions
from . import helpers

urlpatterns = [
    path('', include(router.urls)),
    path('alta', ArticuloCreateView.as_view(), name='ArticuloCreateView'),
    path('listado', ArticuloListView.as_view(), name='ArticuloListView'),
    path('editar/<int:pk>', ArticuloUpdateView.as_view(), name='ArticuloUpdateView'),
    path('eliminar/<int:pk>', ArticuloDeleteView.as_view(), name='ArticuloDeleteView'),
    path('detalle/<int:pk>', ArticuloDetailView.as_view(), name='ArticuloDetailView'),
    path('imprimir/pdf/',ArticuloReportePDF.as_view(), name="ArticuloReportePDF"),
    path('complementos/marca/alta', helpers.guardar_marca, name='guardar_marca'),
    path('complementos/rubro/alta', helpers.guardar_rubro, name='guardar_rubro'),
]
