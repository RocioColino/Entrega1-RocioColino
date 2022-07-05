from django.db import models

class Doctores(models.Model):
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    especialidad=models.CharField(max_length=40)

class Restaurantes(models.Model):
    nombre=models.CharField(max_length=40)
    telefono=models.IntegerField()
    tipoDeComida=models.CharField(max_length=30)

class peluquerias(models.Model):
    nombre=models.CharField(max_length=30)
    telefono=models.IntegerField()
    barrio=models.CharField(max_length=20)

