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

class Facultad(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Programa(models.Model):
    nombre = models.CharField(max_length=50)
    id_facultad = models.ForeignKey(Facultad, on_delete=models.PROTECT,related_name='get_facultad' )

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


class Egresado(models.Model):
    estratos = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
    )

    experiencia = (
        (0, 'menos de 1 año'),
        (1, '1 año'),
        (2, '2 años'),   
        (3, '3 años'),
        (4, '4 años'),
        (5, '5 años'),
        (6, '6 años o mas'),
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
    cargo = models.CharField(max_length=50)
    id_rango_salarial = models.ForeignKey(RangoSalarial,on_delete="PROTECTED")
    id_experiencia = models.IntegerField(choices=experiencia)
    nombre_jefe = models.CharField(max_length=100)

    def __str__(self):
        return self.nombres + " " + self.primer_apellido + " " + self.segundo_apellido

    
class Titulo(models.Model):
    niveles = (
        (1, 'Pregrado'),
        (2, 'Especializacion'),
        (3, 'Maestria'),
        (4, 'Doctorado'),
        (5, 'Post-doctorado'),
        (6, 'MBA'),
        (7, 'Curso'),
        (8, 'Seminario'),
        (9, 'Diplomado'),
        (10, 'Otro'),
    )

    instituciones = (
        (1, 'SENA'),
        (2, 'USB'),
    )

    id_egresado = models.ForeignKey(SituacionLaboralActual, on_delete="CASCADE")
    titulo = models.CharField(max_length=200)
    nivel_academico = models.CharField(max_length=50, choices=niveles)
    institucion = models.CharField(max_length=200, choices=instituciones)
    fecha_graduacion = models.DateField()

    def __str__(self):
        return self.titulo

class Publicacion(models.Model):
    tipos = (
        (1, 'Libro'),
        (2, 'Capítulo'),
        (3, 'Revista'),
        (4, 'Articulo Impreso'),
        (5, 'Articulo Indexado'),
    )

    id_egresado = models.ForeignKey(SituacionLaboralActual, on_delete="CASCADE")
    titulo_publicacion = models.CharField(max_length=200)
    tipo_publicacion = models.CharField(max_length=50, choices=tipos)
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.titulo_publicacion

class Reconocimiento(models.Model):
    instituciones = (
        (1, 'SENA'),
        (2, 'USB'),
    )

    id_egresado = models.ForeignKey(SituacionLaboralActual, on_delete="CASCADE")
    titulo_reconocimiento = models.CharField(max_length=200)
    institucion = models.CharField(max_length=200, choices=instituciones)
    fecha_reconocimiento = models.DateField()

    def __str__(self):
        return self.titulo_reconocimiento

class Participacion(models.Model):
    redes = (
        (1, 'Asociación Artistica'),
        (2, 'Asociación Téctnica/Tecnológica'),
        (3, 'Asociación Científica'),
        (4, 'Asociación Profesional'),
        (5, 'Asociación Sector Productiva'),
        (6, 'Comunidad Académica'),
        (7, 'Asociación Sector Financiero'),
        (8, 'Otra'),
    )

    id_egresado = models.ForeignKey(SituacionLaboralActual, on_delete="CASCADE")
    red = models.CharField(max_length=50, choices=redes)
    descripcion = models.CharField(max_length=200)
    internacional = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion