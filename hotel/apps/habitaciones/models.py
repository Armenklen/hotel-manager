from django.db import models
from datetime import datetime

# Create your models here.
class Habitacion(models.Model):
    tipo=models.CharField(max_length=50)
    cantidad=models.IntegerField()
    precio=models.FloatField()
    descripcion=models.CharField(max_length=200)
    moneda=models.CharField(max_length=100)
    def __unicode__(self):
        return self.tipo
class Mantencion(models.Model):
    habi=models.ForeignKey(Habitacion)
    estado=models.BooleanField()
    tiempo=models.DateField()
    def __unicode__(self):
        return self.habi
class Servicio(models.Model):
    tipo_servicio=models.CharField(max_length=200)
    precio=models.FloatField()
    cantidad=models.IntegerField()
    precio_total=models.FloatField()
    def __unicode__(self):
        return self.tipo_servicio



