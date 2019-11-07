from django.db import models

# Create your models here.

class Tipo_Producto(models.Model):
    nombre = models.CharField(max_length = 200)

    def __init__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length = 200)
    descripcion = models.CharField(max_length = 200)
    tipo   = models.ForeignKey(Tipo_Producto, on_delete=models.PROTECT)

    def __init__(self):
        return self.nombre
