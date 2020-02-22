from django.urls import path

from .views import ArticuloCreateView, ArticuloListView

urlpatterns = [
    path('alta', ArticuloCreateView.as_view(), name='ArticuloCreateView'),
    path('listado', ArticuloListView.as_view(), name='ArticuloListView'),
]
