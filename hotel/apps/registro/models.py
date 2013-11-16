from django.db import models
from django import forms
# Create your models here.
class Registro(models.Model):
	nombre=models.CharField(max_length=150)
	email=models.EmailField()
	password=models.CharField(max_length=150)
	fecha=models.DateField()
	hora=models.TimeField()
	ci=models.CharField(max_length=20)
	def __unicode__(self):
		return self.nombre