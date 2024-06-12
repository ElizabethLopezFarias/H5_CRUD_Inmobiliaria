from django.shortcuts import render, redirect
from .models import Inmuebles
from .forms import RegisterForm, DireccionForm, UbicacionForm, UsuarioForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.shortcuts import HttpResponse, HttpResponseRedirect

# Vista inicio
def indexView(request):
	inmuebles = Inmuebles.objects.all()
	context = {
		'inmuebles': inmuebles
	}
	return render(request, 'index.html', context)

#Vista registro
def register_view(request):
    #indica si el usuario ha iniciado sesión (True) o no (False).
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    if request.method == 'POST':
        register_form = RegisterForm(request.POST)
        usuario_form= UsuarioForm(request.POST)
        direccion_form = DireccionForm(request.POST)
        ubicacion_form = UbicacionForm(request.POST)
        if register_form.is_valid and usuario_form.is_valid() and direccion_form.is_valid() and ubicacion_form.is_valid():
            ubicacion = ubicacion_form.save()
            direccion = direccion_form.save()
            direccion.id_ubicacion = ubicacion
            direccion.save()
            usuario = usuario_form.save(commit=False)
            usuario.id_direccion = direccion
            usuario.save()
            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password1"]
            ultimo_usuario_creado = authenticate(request,username=username,password=password)
            login(request,ultimo_usuario_creado)  
            messages.success(request, 'Usuario registrado exitosamente.')
            return HttpResponseRedirect('login_url')
                
        context = {
                 'register_form': register_form,
                 'usuario_form' : usuario_form,
                 'direccion_form' : direccion_form,
                 'ubicacion_form' : ubicacion_form
                 }  
        return render(request,'registration/register.html', context)
    else:
        register_form = RegisterForm()
        usuario_form = UsuarioForm()
        direccion_form = DireccionForm()
        ubicacion_form = UbicacionForm()
        return render(request, 'registration/register.html', {

    })