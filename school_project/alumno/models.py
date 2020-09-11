from django.db import models


# Create your models here.
class Alumno(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_alumnos = models.CharField(max_length=80, null=False)
    dni_alumnos = models.IntegerField(unique=True, null=False)
    cuil_alumnos = models.IntegerField(null=False, unique=True)
    domicilio_alumnos = models.CharField(max_length=120, null=False)
    email_alumno = models.EmailField(null=False)
    num_contacto_alumno = models.IntegerField(null=False)
    # discapacidad_alumno = models.CharField(max_length=120)      podria ser boolean
    curso_alumno = models.CharField(max_length=4, default='nn')
    num_legajo_alumno = models.CharField(max_length=30, unique=True, null=False)
    nombre_tutor = models.CharField(max_length=80, null=False)
    dni_tutor = models.IntegerField(unique=True, null=False)
    num_contacto_tutor = models.IntegerField(null=False)
    observacion_general = models.TextField(blank=False, default='inserte la observacion del alumno aquí')
    plan_ano_alumno = models.CharField(max_length=80, null=False)
    especialidad_alumno = models.CharField(max_length=80, null=False)
