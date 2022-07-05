from django.urls import path
from AppCoder import views
from AppCoder.views import Doctores, Peluquerias, Restaurantes, inicio

urlpattern=[
    path('doctores/', Doctores),
    path('peluquerias/', Peluquerias),
    path('restaurantes/', Restaurantes),
    path('inicio/', inicio),
]