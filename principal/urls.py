from django.contrib import admin
from django.urls import path
from principal import views

urlpatterns = [
 path('principal/',views.principal),
]
