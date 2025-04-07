from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def foro(request):
    return render(request, 'forowiki.html')

def registrarse(request):
    return render(request, 'registrase_wiki.html')

def inicio_sesion(request):
    return render(request, 'inicio_sesion_wiki.html')

def mi_cuenta(request):
    return render(request, 'micuentatf.html')

def recuperar_contraseña(request):
    return render(request, 'recuperarcontra.html')