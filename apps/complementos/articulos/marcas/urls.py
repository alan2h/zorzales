from .views import MarcaCreateView, MarcaListView, MarcaDeleteView, MarcaUpdateView
from django.urls import path

urlpatterns = [
    path('alta', MarcaCreateView.as_view(), name='MarcaCreateView'),
    path('listado', MarcaListView.as_view(), name='MarcaListView'),
    path('eliminar/<int:pk>', MarcaDeleteView.as_view(), name='MarcaDeleteView'),
    path('editar/<int:pk>', MarcaUpdateView.as_view(), name='MarcaUpdateView'),
]
