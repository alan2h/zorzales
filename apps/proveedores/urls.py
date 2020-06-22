from django.urls import path, include

from .views import ProveedorListView

urlpatterns = [
    path('listado', ProveedorListView.as_view(), name='ProveedorListView'),
]
