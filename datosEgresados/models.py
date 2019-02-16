from django.db import models

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Departamento(models.Model):
    nombre = models.CharField(max_length=50)
    id_pais = models.ForeignKey(Pais, on_delete=models.PROTECT,related_name='get_pais' )

    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=50)
    id_departamento = models.ForeignKey(Departamento, on_delete=models.PROTECT,related_name='get_departamento' )

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    id_facultad = models.ForeignKey(Facultad, on_delete=models.PROTECT,related_name='get_facultad' )

    def __str__(self):
        return self.nombre

class Facultad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class SituacionLaboralActual(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class AreaTrabajo(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class RangoSalarial(models.Model):
    detalle = models.CharField(max_length=50)

    def __str__(self):
        return self.detalle

class Experiencia(models.Model):
    detalle = models.CharField(max_length=50)

    def __str__(self):
        return self.detalle