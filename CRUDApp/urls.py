from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.crud, name="CRUD"),
    path('leer_post', views.crud, name="Leer"),
]
