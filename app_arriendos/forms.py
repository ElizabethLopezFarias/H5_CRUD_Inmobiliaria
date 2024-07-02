from django import forms
from django.contrib.auth.models import User
from .models import Usuarios, Direccion, Ubicacion
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre', 
            'last_name': 'Apellido',
            'email':'Correo electronico', 
            'password1':'Contraseña', 
            'password2':'Repita la contraseña'
        }
    
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ('tipo_usuario','rut','telefono')


class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'depto']


class UbicacionForm(forms.ModelForm):
#     #carga de region y comuna mediante lista de opciones
    comuna_region = forms.ModelChoiceField(queryset=Ubicacion.objects.all(), empty_label="Seleccione Comuna y Región")
    

    class Meta:
        model = Ubicacion
        fields = ['comuna_region']

    

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        labels = {
            'username':'Nombre de Usuario',
            'first_name':'Nombre', 
            'last_name': 'Apellido',
            'email':'Correo electronico', 
        } 

