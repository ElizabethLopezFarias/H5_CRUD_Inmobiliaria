from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, editar_perfil, load_comunas


urlpatterns = [
    path('', views.indexView, name='home'),
    path('login/', LoginView.as_view(next_page='home'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('register/', register_view, name='register'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),

]