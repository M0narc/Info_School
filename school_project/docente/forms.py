from django import forms

from .models import Docente

class Docente_forma(forms.ModelForm):
    class Meta:
        mode = Docente
        fields =[
            'nombre_docente'
            'dni'
        ]

