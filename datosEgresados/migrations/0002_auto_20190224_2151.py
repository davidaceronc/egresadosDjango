# Generated by Django 2.1.7 on 2019-02-25 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datosEgresados', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participaciones',
            new_name='Participacion',
        ),
        migrations.RenameModel(
            old_name='Reconocimientos',
            new_name='Reconocimiento',
        ),
    ]
