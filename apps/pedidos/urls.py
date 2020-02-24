from django.urls import path

from .views import PedidoCreateView

urlpatterns = [
    path('alta', PedidoCreateView.as_view(), name='PedidoCreateView')
]
