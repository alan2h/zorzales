from django.urls import path, include
from rest_framework import routers

from .views import ClienteCreateView, ClientesListView, ClienteUpdateView, ClienteDeleteView

from .viewsets import ClienteViewSet

router = routers.DefaultRouter()
router.register(r'api', ClienteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('alta', ClienteCreateView.as_view(), name='ClienteCreateView'),
    path('listado', ClientesListView.as_view(), name='ClientesListView'),
    path('actualizar/<int:pk>', ClienteUpdateView.as_view(), name='ClienteUpdateView'),
    path('eliminar/<int:pk>', ClienteDeleteView.as_view(), name='ClienteDeleteView')
]
