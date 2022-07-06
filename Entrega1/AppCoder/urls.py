from django.contrib import admin
from django.urls import path, include
from . import views 


urlpatterns = [    
    path('',views.inicio, name="inicio"),
    path('doctores/', views.doctores, name="doctores"),
    path('restaurantes/', views.restaurantes, name="restaurantes"),
    path('peluquerias/',views.peluquerias, name="peluquerias"),
]

