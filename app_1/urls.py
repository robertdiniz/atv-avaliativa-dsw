from django.urls import path
from .views import index, editar, cadastro

urlpatterns = [
    path('', index, name="index"),
    path('editar/<int:pk>', editar, name="editar"),
    path('cadastro', cadastro, name="cadastro"),
]
