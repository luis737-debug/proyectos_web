from django.contrib import admin
from django.urls import path
from  login import views

urlpatterns = [
    path('validar/',views.validaruser),
    path('',views.login),
]
