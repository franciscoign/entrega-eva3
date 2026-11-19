from django import forms
from .models import Socio


class SocioForm(forms.ModelForm):
    class Meta:
        model = Socio
        fields = ['nombre', 'edad', 'plan', 'fecha_inscripcion', 'activo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'plan': forms.Select(attrs={'class': 'form-select'}),
            'fecha_inscripcion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}, format='%Y-%m-%d'),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
