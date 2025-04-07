
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home , name='home'),
    path('foro/', views.foro , name='foro'),
    path('registrarse/', views.registrarse , name='registrarse'),
    path('inicio_sesion/', views.inicio_sesion , name='inicio_sesion'),
    path('mi_cuenta/', views.mi_cuenta , name='mi_cuenta'),
    path('recuperar_contraseña/', views.recuperar_contraseña , name='recuperar_contraseña'),

    
]
