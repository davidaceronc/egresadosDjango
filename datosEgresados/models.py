from django.db import models

# Create your models here.
class Egresado(models.Model):

    estratos = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )
    afinidad = ((True, 'Si'), (False, 'No'))

    id = models.CharField(max_length=15, primary_key=True)
    primer_apellido = models.CharField(max_length=20)
    segundo_apellido = models.CharField(max_length=20)
    nombres = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    programa = models.ForeignKey(Programa, on_delete="PROTECTED")
    lugar_nac = models.CharField(max_length=100)
    id_ciudad_res = models.ForeignKey(Ciudad, on_delete='PROTECTED')
    direccion_res = models.CharField(max_length=100)
    telefono_res = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    id_estado_civil = models.ForeignKey(EstadoCivil, on_delete='PROTECTED')
    estrato = models.IntegerField(choices=estratos)
    email = models.CharField(max_length=50)
    email2 = models.CharField(max_length=50)
    situacion_lab_actual = models.ForeignKey(SituacionLaboralActual, on_delete="PROTECTED")
    id_area_trabajo = models.ForeignKey(AreaTrabajo, on_delete="PROTECTED")
    afin = models.BooleanField(choices=afinidad, default=True)
    empresa = models.CharField(max_length=50)
    direccion_empresa = models.CharField(max_length=50)
    telefono_empresa = models.CharField(max_length=50)
    ext = models.IntegerField()
    cargo = models.CharField(max_lenght=50)
    id_rango_salarial = models.ForeignKey(RangoSalarial,on_delete="PROTECTED")
    id_experiencia = models.ForeignKey(Experiencia,on_delete="PROTECTED")
    nombre_jefe = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres + " " + self.primer_apellido + " " + self.segundo_apellido