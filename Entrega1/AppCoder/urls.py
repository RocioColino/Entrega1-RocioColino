from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [    
    path('inicio/', inicio),
    path('doctores/', doctores),
    path('restaurantes/', restaurantes),
    path('peluquerias/', peluquerias),
]

