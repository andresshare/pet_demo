from django import forms
from mascota.models import Mascota


class Mascota_form(forms.ModelForm):

    class Meta:
        model  = Mascota

        fields =[

        'nombre',
        'sexo',
        'edad_aproximada',
        'fecha_rescate',
        'persona',
        'vacuna',
        ]

        labels= {
            'nombre': 'Nombre',
            'sexo': 'sexo',
            'edad_aproximada':'Edad',
            'fecha_rescate':'Fecha de rescate',
            'persona':'Adoptante',
            'vacuna':'vacunas',
        }

        widgets = {

            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo':forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada':forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate':forms.TextInput(attrs={'class':'form-control'}),
            'persona':forms.Select(attrs={'class':'form-control'}),
            'vacuna':forms.CheckboxSelectMultiple(),

        }
