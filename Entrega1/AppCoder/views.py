from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import *

def inicio(request):
   # return HttpResponse("vista inicio")
   return render(request, "AppCoder/index.html",{})

def doctores(request):
    return render(request,'AppCoder/doctores.html',{})

def restaurantes(request):
    return render(request,'AppCoder/restaurantes.html',{})

def peluquerias(request):
    return render(request,'AppCoder/peluquerias.html',{})
