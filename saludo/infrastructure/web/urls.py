from django.urls import path
from .views import saludar_view

urlpatterns = [path("hola/", saludar_view, name="saludar")]
