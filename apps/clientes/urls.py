from django.urls import path

from .views import ClienteCreateView, ClientesListView

urlpatterns = [
    path('alta', ClienteCreateView.as_view(), name='ClienteCreateView'),
    path('listado', ClientesListView.as_view(), name='ClientesListView')
]
