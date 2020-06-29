
from django.urls import include, path
from rest_framework import routers

from .views import CompraTemplateView

from .viewsets import CompraViewSet

router = routers.DefaultRouter()
router.register(r'api', CompraViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('base', CompraTemplateView.as_view(), name="CompraTemplateView")
]
