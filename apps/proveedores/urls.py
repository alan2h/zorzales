from django.urls import path, include

from .views import (
                    ProveedorListView, 
                    ProveedorCreateView,
                    ProveedorUpdateView,
                    ContactoCreateView,
                    ProveedorDetailView,
                    ContactoDeleteView
                    )

urlpatterns = [
    path('listado', ProveedorListView.as_view(), name='ProveedorListView'),
    path('alta', ProveedorCreateView.as_view(), name='ProveedorCreateView'),
    path('editar/<int:pk>', ProveedorUpdateView.as_view(), name='ProveedorUpdateView'),
    path('detalle/<int:pk>', ProveedorDetailView.as_view(), name='ProveedorDetailView'),
    # contactos
    path('contactos/<int:id_proveedor>', ContactoCreateView.as_view(), name='ContactoCreateView'),
    path('contactos/eliminar/<int:pk>', ContactoDeleteView.as_view(), name='ContactoDeleteView'),
]
