# Generated by Django 2.1.2 on 2019-02-23 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AreaTrabajo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('primer_apellido', models.CharField(max_length=20)),
                ('segundo_apellido', models.CharField(max_length=20)),
                ('nombres', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField()),
                ('lugar_nac', models.CharField(max_length=100)),
                ('direccion_res', models.CharField(max_length=100)),
                ('telefono_res', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('estrato', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')])),
                ('email', models.CharField(max_length=50)),
                ('email2', models.CharField(max_length=50)),
                ('afin', models.BooleanField(choices=[(True, 'Si'), (False, 'No')], default=True)),
                ('empresa', models.CharField(max_length=50)),
                ('direccion_empresa', models.CharField(max_length=50)),
                ('telefono_empresa', models.CharField(max_length=50)),
                ('ext', models.IntegerField()),
                ('cargo', models.CharField(max_length=50)),
                ('id_experiencia', models.IntegerField(choices=[(0, 'menos de 1 año'), (1, '1 año'), (2, '2 años'), (3, '3 años'), (4, '4 años'), (5, '5 años'), (6, '6 años o mas')])),
                ('nombre_jefe', models.CharField(max_length=100)),
                ('id_area_trabajo', models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.AreaTrabajo')),
                ('id_ciudad_res', models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.Ciudad')),
            ],
        ),
        migrations.CreateModel(
            name='EstadoCivil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Experiencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participaciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('red', models.CharField(choices=[(1, 'Asociación Artistica'), (2, 'Asociación Téctnica/Tecnológica'), (3, 'Asociación Científica'), (4, 'Asociación Profesional'), (5, 'Asociación Sector Productiva'), (6, 'Comunidad Académica'), (7, 'Asociación Sector Financiero'), (8, 'Otra')], max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
                ('internacional', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('id_facultad', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_facultad', to='datosEgresados.Facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_publicacion', models.CharField(max_length=200)),
                ('tipo_publicacion', models.CharField(choices=[(1, 'Libro'), (2, 'Capítulo'), (3, 'Revista'), (4, 'Articulo Impreso'), (5, 'Articulo Indexado')], max_length=50)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RangoSalarial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detalle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reconocimientos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_reconocimiento', models.CharField(max_length=200)),
                ('institucion', models.CharField(choices=[(1, 'SENA'), (2, 'USB')], max_length=200)),
                ('fecha_reconocimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='SituacionLaboralActual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Titulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('nivel_academico', models.CharField(choices=[(1, 'Pregrado'), (2, 'Especializacion'), (3, 'Maestria'), (4, 'Doctorado'), (5, 'Post-doctorado'), (6, 'MBA'), (7, 'Curso'), (8, 'Seminario'), (9, 'Diplomado'), (10, 'Otro')], max_length=50)),
                ('institucion', models.CharField(choices=[(1, 'SENA'), (2, 'USB')], max_length=200)),
                ('fecha_graduacion', models.DateField()),
                ('id_egresado', models.ForeignKey(on_delete='CASCADE', to='datosEgresados.SituacionLaboralActual')),
            ],
        ),
        migrations.AddField(
            model_name='reconocimientos',
            name='id_egresado',
            field=models.ForeignKey(on_delete='CASCADE', to='datosEgresados.SituacionLaboralActual'),
        ),
        migrations.AddField(
            model_name='publicacion',
            name='id_egresado',
            field=models.ForeignKey(on_delete='CASCADE', to='datosEgresados.SituacionLaboralActual'),
        ),
        migrations.AddField(
            model_name='participaciones',
            name='id_egresado',
            field=models.ForeignKey(on_delete='CASCADE', to='datosEgresados.SituacionLaboralActual'),
        ),
        migrations.AddField(
            model_name='egresado',
            name='id_estado_civil',
            field=models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.EstadoCivil'),
        ),
        migrations.AddField(
            model_name='egresado',
            name='id_rango_salarial',
            field=models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.RangoSalarial'),
        ),
        migrations.AddField(
            model_name='egresado',
            name='programa',
            field=models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.Programa'),
        ),
        migrations.AddField(
            model_name='egresado',
            name='situacion_lab_actual',
            field=models.ForeignKey(on_delete='PROTECTED', to='datosEgresados.SituacionLaboralActual'),
        ),
        migrations.AddField(
            model_name='departamento',
            name='id_pais',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_pais', to='datosEgresados.Pais'),
        ),
        migrations.AddField(
            model_name='ciudad',
            name='id_departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='get_departamento', to='datosEgresados.Departamento'),
        ),
    ]
