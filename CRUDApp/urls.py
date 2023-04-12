from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.crud, name="CRUD"),
    path('leer_post/', views.crud, name="Leer"),
    path('post_crear/', views.PostFormView.index, name="post_crear"),
    path('post_guardar/', views.PostFormView.procesar_form, name="guardar_post")
]
