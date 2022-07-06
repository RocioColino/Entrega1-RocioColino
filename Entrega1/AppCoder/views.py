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
    return render(request,'AppCoder/restaurantes.html',{})

def peluquerias(request):
    return render(request,'AppCoder/peluquerias.html',{})

def nuevodoctor(request):
    if request.method == "POST":
        form = NuevoDoctor(request.POST)
        if form.is_valid:
            form.save()
            return redirect('doctores')
    else: 
        form = NuevoDoctor()
    return render(request, 'AppCoder/nuevodoctor.html',{"form":form})
