
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home , name='home'),
    path('foro/', views.foro , name='foro'),
    path('registrarse/', views.registrarse , name='registrarse'),
    path('inicio_sesion/', views.inicio_sesion , name='inicio_sesion'),
    path('mi_cuenta/', views.mi_cuenta , name='mi_cuenta'),
    path('recuperar_contraseña/', views.recuperar_contraseña , name='recuperar_contraseña'),

    path('registrar_usuario/', views.registrar_usuario , name='registrar_usuario'),
    path('login/', views.login , name='login'),
    path('pass_recovery/', views.pass_recovery , name='pass_recovery'),
]
