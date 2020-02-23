from .views import RubroCreateView, RubroListView, RubroUpdateView, \
    RubroDeleteView
from django.urls import path

urlpatterns = [
    path('alta', RubroCreateView.as_view(), name='RubroCreateView'),
    path('listado', RubroListView.as_view(), name='RubroListView'),
    path('editar/<int:pk>', RubroUpdateView.as_view(), name='RubroUpdateView'),
    path('eliminar/<int:pk>', RubroDeleteView.as_view(), name='RubroDeleteView'),
]