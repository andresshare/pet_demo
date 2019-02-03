from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    edad =  models.IntegerField()
    telefono = models.IntegerField()
    email = models.EmailField()
    domicilio = models.TextField()

