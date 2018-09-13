from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	def __str__(self):
		return self.nombre

class Evento(models.Model):
	nombre = models.CharField(max_length = 100)
	lugar = models.CharField(max_length = 100,)
	fecha_evento = models.DateField()
	descripcion = models.CharField(max_length = 1000,)
	usuario = models.ForeignKey(Usuario,on_delete = models.PROTECT)
	def __str__(self):
		return self.nombre


class Galeria(models.Model):
	nombre = models.CharField(max_length = 100)
	path = models.ImageField(upload_to = 'fotos', null = True, blank = True)
	evento  = models.ForeignKey(Evento, on_delete = models.CASCADE)
	def __str__(self):
		return self.nombre

class Participante(models.Model):
	nombre = models.CharField(max_length = 100)
	apellido = models.CharField(max_length = 100)
	email = models.CharField(max_length = 100)
	telefono = models.CharField(max_length = 20)
	def __str__(self):
		return self.nombre

class ParticipanteEvento(models.Model):
	participante = models.ForeignKey(Participante,on_delete=models.PROTECT)
	evento = models.ForeignKey(Evento,on_delete=models.PROTECT)