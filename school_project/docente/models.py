from django.db import models
from django.utils import timezone


# Create your models here.
class Docente(models.Model):
    id   =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_docente =  models.CharField(max_length=80)
    dni  =  models.PositiveIntegerField(unique=True, blank=False)
    secu_bla = models.TextField(blank=False)
    asignacion =    models.CharField(blank=False, max_length=80)
    anexo = models.TextField(blank=False)
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
