from django.urls import path, include

from .views import ProveedorListView, ProveedorCreateView

urlpatterns = [
    path('listado', ProveedorListView.as_view(), name='ProveedorListView'),
    path('alta', ProveedorCreateView.as_view(), name='ProveedorCreateView'),
]
