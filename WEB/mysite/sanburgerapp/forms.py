
from django import forms
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class FormularioUser(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['edad', 'telefono', 'correo', 'domicilio', 'numero_tarjeta', 'titular_tarjeta', 'caducidad_tarjeta', 'cvv_tarjeta']

    edad = forms.IntegerField(required=False)
    telefono = forms.IntegerField(required=False)
    correo = forms.CharField(max_length=30, required=False)
    domicilio = forms.CharField(max_length=50, required=False)
    numero_tarjeta = forms.IntegerField(required=False)
    titular_tarjeta = forms.CharField(max_length=30, required=False)
    caducidad_tarjeta = forms.DateField(required=False)
    cvv_tarjeta = forms.IntegerField(required=False)