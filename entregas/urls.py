from django.urls import path
from . import views

urlpatterns = [
    path("hola/", views.hola, name="hola"),
    path("cotizar/", views.cotizar, name="cotizar"),
]
