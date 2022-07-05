from django.shortcuts import render
from django.http import HttpResponse


def Doctores(self):
    doctores=Doctores(nombre="Kim",telefono="01077668855", especialidad="General")
    doctores.save()
    documentoDeTexto=f"Doctor: {doctores.nombre}    Telefono: {doctores.telefono}   Especialidad: {doctores.especialidad}"
    return HttpResponse(documentoDeTexto)

def Peluquerias(self):
    peluquerias=Peluquerias(nombre="Park", telefono="01033556677", barrio="Dongdemun")
    peluquerias.save()
    documentoDeTexto=f"Peluqueria: {peluquerias.nombre} Telefono: {peluquerias.telefono}    Barrio: {peluquerias.barrio}"
    return HttpResponse(documentoDeTexto)

def Restaurantes(self):
    restaurantes=Restaurantes(nombre="Sikdang", telefono="01012345678", tipoDeComida="Coreana")
    restaurantes.save()
    documentoDeTexto=f"Restaurante: {restaurantes.nombre}    Telefono: {restaurantes.telefono}  Especialidad: {restaurantes.tipoDeComida}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")



