# Generated by Django 3.2.6 on 2021-08-09 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Carreras',
            new_name='Carrera',
        ),
        migrations.RenameModel(
            old_name='Cursos',
            new_name='Curso',
        ),
        migrations.RenameModel(
            old_name='Estudiantes',
            new_name='Estudiante',
        ),
        migrations.RenameModel(
            old_name='Matriculas',
            new_name='Matricula',
        ),
    ]
