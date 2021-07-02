from django.forms import fields
from .models import Alumno
from django import forms

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['first_name', 'last_name', 'email', 'phone', 'generacion']
        widgets = {
            
            "email" : forms.EmailInput()
        }