from django.urls import path

from .views import ArticuloCreateView

urlpatterns = [
    path('alta', ArticuloCreateView.as_view(), name='ArticuloCreateView')
]
