from django.urls import path

from .views import ClienteCreateView, ClientesListView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('alta', ClienteCreateView.as_view(), name='ClienteCreateView'),
    path('listado', ClientesListView.as_view(), name='ClientesListView'),
    path('actualizar/<int:pk>', ClienteUpdateView.as_view(), name='ClienteUpdateView'),
    path('eliminar/<int:pk>', ClienteDeleteView.as_view(), name='ClienteDeleteView')
]
