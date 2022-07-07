from django.shortcuts import render, redirect
from django.http import HttpResponse
from AppCoder.models import *
from .forms import *


def inicio(request):
   # return HttpResponse("vista inicio")
   return render(request, "AppCoder/index.html",{})

def doctores(request):
    doctores=Doctores.objects.all()
    return render(request,'AppCoder/doctores.html',{"doctores":doctores})

def restaurantes(request):
    restaurantes=Restaurantes.objects.all()
    return render(request,'AppCoder/restaurantes.html',{"restaurantes":restaurantes})

def peluquerias(request):
    peluquerias=Peluquerias.objects.all()
    return render(request,'AppCoder/peluquerias.html',{"peluquerias":peluquerias})

def nuevodoctor(request):
    if request.method == "POST":
        form = NuevoDoctor(request.POST)
        if form.is_valid:
            form.save()
            return redirect('doctores')
    else: 
        form = NuevoDoctor()
    return render(request, 'AppCoder/nuevodoctor.html',{"form":form})

def nuevapeluqueria(request):
    if request.method == "POST":
        form = NuevaPeluqueria(request.POST)
        if form.is_valid:
            form.save()
            return redirect('peluquerias')
    else: 
        form = NuevaPeluqueria()
    return render(request, 'AppCoder/nuevapeluqueria.html',{"form":form})

def nuevorestaurante(request):
    if request.method == "POST":
        form = NuevoRestaurante(request.POST)
        if form.is_valid:
            form.save()
            return redirect('restaurantes')
    else: 
        form = NuevoRestaurante()
    return render(request, 'AppCoder/nuevorestaurante.html',{"form":form})

def busqueda_restaurante(request):
    if request.method=="POST":
        restaurantes=request.POST["restaurantes"]
        restaurantes=restaurantes.objects.filter(restaurantes__icontains=restaurantes)
        return render(request,"AppCoder/busqueda_restaurante.html", {"restaurantes":restaurantes})
    else:
        restaurantes=[]
    return render(request,"AppCoder/busqueda_restaurante.html", {"restaurantes":restaurantes})