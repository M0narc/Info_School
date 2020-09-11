from django.db import models


# Create your models here.
class Alumno(models.Model):
    ANO_ALUMNO =(
        ('1', 'Año 1'),
        ('2', 'Año 2'),
        ('3', 'Año 3'),
        ('4', 'Año 4'),
    )

    CURSOS_ALUMNO = (
        ('A', 'Curso A'),
        ('B', 'Curso B'),
        ('C', 'Curso C'),
    )
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_alumnos = models.CharField(max_length=80, null=False)
    dni_alumnos = models.PositiveIntegerField(unique=True, null=False)
    cuil_alumnos = models.PositiveIntegerField(null=False, unique=True)
    domicilio_alumnos = models.CharField(max_length=120, null=False)
    email_alumno = models.EmailField(null=False)
    num_contacto_alumno = models.PositiveIntegerField(null=False)
    # discapacidad_alumno = models.CharField(max_length=120)      podria ser choices
    ano_alumno = models.CharField(max_length=1, choices=ANO_ALUMNO, default="1")
    curso_alumno = models.CharField(max_length=1, choices=CURSOS_ALUMNO)   # choices
    num_legajo_alumno = models.CharField(max_length=30, unique=True, null=False)
    nombre_tutor = models.CharField(max_length=80, null=False)
    dni_tutor = models.PositiveIntegerField(unique=True, null=False)
    num_contacto_tutor = models.PositiveIntegerField(null=False)
    observacion_general = models.TextField(blank=False, default='inserte la observacion del alumno aquí')
    plan_ano_alumno = models.CharField(max_length=80, null=False)
    especialidad_alumno = models.CharField(max_length=80, null=False)
