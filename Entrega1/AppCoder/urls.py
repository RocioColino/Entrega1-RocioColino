from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [    
    path('',views.inicio, name="inicio"),
    path('doctores/', views.doctores, name="doctores"),
    path('restaurantes/', views.restaurantes, name="restaurantes"),
    path('peluquerias/',views.peluquerias, name="peluquerias"),
    path('nuevodoctor/',views.nuevodoctor, name="nuevodoctor" ),
    path('nuevapeluqueria/', views.nuevapeluqueria, name="nuevapeluqueria"),
    path('nuevorestaurante/', views.nuevorestaurante, name="nuevorestaurante"),
    path('busqueda_restaurante/', views.busqueda_restaurante, name="busqueda_restaurante"),
]

