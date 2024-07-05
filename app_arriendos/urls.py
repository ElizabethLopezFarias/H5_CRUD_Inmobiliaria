from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, editar_perfil, agregar_inmueble, editar_inmueble, borrar_inmueble, listar_inmuebles, detalle_inmueble, solicitar_reserva, ver_notificaciones


urlpatterns = [
    path('', views.indexView, name='home'),
    path('login/', LoginView.as_view(next_page='home'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register_view, name='register'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('agregar_inmueble/', agregar_inmueble, name='agregar_inmueble'),
    path('editar_inmueble/<int:id>/', editar_inmueble, name='editar_inmueble'),
    path('borrar_inmueble/<int:id>/', borrar_inmueble, name='borrar_inmueble'),
    path('listar_inmuebles/', listar_inmuebles, name='listar_inmuebles'),
    path('detalle_inmueble/<int:id>/', detalle_inmueble, name='detalle_inmueble'),
    path('solicitar_reserva/<int:inmueble_id>/', solicitar_reserva, name='solicitar_reserva'),
    path('notificaciones/', ver_notificaciones, name='ver_notificaciones'),

]