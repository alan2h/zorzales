from django.urls import path, include

from .views import ReservaView
from .viewsets import ReservaViewSet

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('listado', ReservaView.as_view(), name='ReservaView'),
]
