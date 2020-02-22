from .views import RubroCreateView, RubroListView
from django.urls import path

urlpatterns = [
    path('alta', RubroCreateView.as_view(), name='RubroCreateView'),
    path('listado', RubroListView.as_view(), name='RubroListView'),
]