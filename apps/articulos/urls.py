from django.urls import path

from .views import ArticuloCreateView, ArticuloListView, \
    ArticuloUpdateView, ArticuloDeleteView

urlpatterns = [
    path('alta', ArticuloCreateView.as_view(), name='ArticuloCreateView'),
    path('listado', ArticuloListView.as_view(), name='ArticuloListView'),
    path('editar/<int:pk>', ArticuloUpdateView.as_view(), name='ArticuloUpdateView'),
    path('eliminar/<int:pk>', ArticuloDeleteView.as_view(), name='ArticuloDeleteView'),
]
