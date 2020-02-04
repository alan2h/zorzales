from django.urls import path

from .views import ClienteCreateView

urlpatterns = [
    path('alta', ClienteCreateView.as_view(), name='dashboard')
]
