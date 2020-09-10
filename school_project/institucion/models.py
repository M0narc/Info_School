from django.db import models

# Create your models here.

class Institucion(models.Model):
    id       =    models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    nombre   =    models.CharField(max_length=120, blank=False)
    cue =   models.CharField(max_length=120, blank=False, null=False)
    domicilio = models.CharField(max_length=120, blank=False)
    telefono =  models.IntegerField(max_length=20, blank=False)
    email = models.EmailField()
    facebook =  models.CharField(max_length=120)
    modalidad = models.CharField(max_length=120)
    plan_estudio =  models.TextField(blank=False)
