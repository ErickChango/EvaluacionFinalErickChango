from django import forms
from .models import Juego

class JuegoForm(forms.ModelForm):
    class Meta:
        model = Juego
        fields = ['titulo', 'genero', 'plataforma', 'anio']
        labels = {
            'titulo': 'Título',
            'genero': 'Género',
            'plataforma': 'Plataforma',
            'anio': 'Año',
        }
