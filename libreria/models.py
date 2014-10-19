from django.db import models
from django.contrib.auth.models import User

class Autor(models.Model):
    apellidos = models.CharField(max_length=128)
    nombre = models.CharField(max_length=128)
    fecha_nacimiento = models.DateField()

    def __unicode__(self):
        return self.apellidos + ", " + self.nombre

    class Meta:
        unique_together = (("apellidos", "nombre"),)


class Genero(models.Model):
    nombre = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.nombre


class Estanteria(models.Model):
    nombre = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.nombre


class Libro(models.Model):
    nombre = models.CharField(max_length=128, unique=True)
    fecha_publicacion = models.IntegerField(default=0)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    genero = models.ForeignKey(Genero, on_delete=models.PROTECT)
    estanteria = models.ForeignKey(Estanteria, on_delete=models.PROTECT)

    def __unicode__(self):
        return self.nombre

class UltimaLectura(models.Model):
    fecha = models.DateField()

class UserProfile(models.Model):
    user = models.OneToOneField(User)

    def __unicode__(self):
        return self.username



