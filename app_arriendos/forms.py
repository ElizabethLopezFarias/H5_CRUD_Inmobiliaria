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
        fields = ('tipo_usuario','rut','id_direccion','telefono')



class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['calle', 'numero', 'depto', 'id_ubicacion']

class UbicacionForm(forms.ModelForm):
    class Meta:
        model = Ubicacion
        fields = ['nombre_region', 'nombre_comuna']

# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = Usuarios
#         fields = ['nombre', 'apellido', 'telefono', 'correo']        

