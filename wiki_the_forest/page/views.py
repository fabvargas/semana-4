import json
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import User

# Create your views here.

def home(request):
    user_email = request.session.get('user_email',None)
    return render(request, 'home.html', {'user_email': user_email})

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

@csrf_exempt  # Solo para pruebas. Usa CSRF en producción
def registrar_usuario(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('contrasena')
            confirm_password = data.get('confirmContrasena')

            if not email or not password or not confirm_password:
                return JsonResponse({'status': 'error', 'message': 'Todos los campos son obligatorios.'}, status=400)

            if password != confirm_password:
                return JsonResponse({'status': 'error', 'message': 'Las contraseñas no coinciden.'}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({'status': 'error', 'message': 'Este correo ya está registrado.'}, status=400)

            hashed_password = make_password(password)
            user = User(password=hashed_password, email=email)
            user.save()

            return JsonResponse({'status': 'success', 'message': 'Usuario registrado correctamente.'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Datos JSON inválidos.'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt  # Para pruebas. En producción, protege con CSRF
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            password = data.get('contrasena')
            
          

            if not email or not password:
                return JsonResponse({'success': False, 'error': 'Todos los campos son obligatorios.'}, status=400)

            user = User.objects.filter(email=email).first()
            

            if user and check_password(password, user.password):
                
                request.session['user_id'] = user.user_id 
                request.session['user_email'] = user.email
                
                return JsonResponse({'success': True})
            else:
                return JsonResponse({'success': False, 'error': 'Credenciales incorrectas.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos JSON inválidos.'}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)

@csrf_exempt
def pass_recovery(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)

            email = data.get('email')
            nueva_contrasena = data.get('contrasena')

            if not email or not nueva_contrasena:
                return JsonResponse({'success': False, 'error': 'Correo y contraseña son obligatorios.'}, status=400)

            user = User.objects.filter(email=email).first()

            if not user:
                return JsonResponse({'success': False, 'error': 'Usuario no encontrado.'}, status=404)

            # Hashear la nueva contraseña y guardarla
            hashed_password = make_password(nueva_contrasena)
            user.password = hashed_password
            user.save()

            return JsonResponse({'success': True, 'message': 'Contraseña actualizada correctamente.'})

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'error': 'Datos inválidos.'}, status=400)

    return JsonResponse({'success': False, 'error': 'Método no permitido.'}, status=405)


def logout(request):
    request.session.flush()
    return redirect('home')