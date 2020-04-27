from django.urls import path, include

from .viewsets import CabaniaViewSet
from .views import  MapaView

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', CabaniaViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('mapa', MapaView.as_view(), name='MapaView'),
]
