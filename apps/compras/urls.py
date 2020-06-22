
from django.urls import include, path

from .views import CompraTemplateView

urlpatterns = [
    path('base', CompraTemplateView.as_view(), name="CompraTemplateView")
]
