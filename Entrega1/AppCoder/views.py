from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return HttpResponse("vista inicio")

def doctores(request):
    return HttpResponse('vista doctores')

def restaurantes(request):
    return HttpResponse('vista restaurantes')

def peluquerias(request):
    return HttpResponse('vista peluquerias')
    