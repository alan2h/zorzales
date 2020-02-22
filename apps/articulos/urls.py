from django.urls import path

from .views import ArticuloCreateView, ArticuloListView, \
    ArticuloUpdateView, ArticuloDeleteView, ArticuloDetailView, ArticuloReportePDF

urlpatterns = [
    path('alta', ArticuloCreateView.as_view(), name='ArticuloCreateView'),
    path('listado', ArticuloListView.as_view(), name='ArticuloListView'),
    path('editar/<int:pk>', ArticuloUpdateView.as_view(), name='ArticuloUpdateView'),
    path('detalle/<int:pk>', ArticuloDetailView.as_view(), name='ArticuloDetailView'),
    path('imprimir/pdf/',ArticuloReportePDF.as_view(), name="ArticuloReportePDF"),
]
