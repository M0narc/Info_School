from django.db import models
from django.utils import timezone


# Create your models here.
class Docente(models.Model):
    id   =  models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre_docente =  models.CharField(max_length=120)
    dni  =  models.IntegerField(unique=True)
    secu_bla = models.TextField(blank=False)
    asignacion =    models.TextField(blank=False)
    anexo = models.TextField(blank=False)
    fecha_de_creacion = models.DateTimeField(default=timezone.now)
