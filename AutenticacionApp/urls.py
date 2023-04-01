from django.urls import path
from .views import VistaRegistro, cerrar_sesion, inicio_sesion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', VistaRegistro.as_view(), name="Registro"),
    path('cerrar_cesion', cerrar_sesion, name="cerrar_sesion"),
    path('login', inicio_sesion, name="inicio_sesion"),
]
