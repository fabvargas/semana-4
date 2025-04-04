
from django.urls import path
from . import views

urlpatterns = [
    
    path('lugares/', views.lugares , name='lugares'),
    path('historia/', views.historia , name='historia'),
    path('flora/', views.flora , name='flora'),
    path('enemigos/', views.enemigos , name='enemigos'),
    path('animales/', views.animales , name='animales'),
    path('armas/', views.armas , name='armas'),
    path('construccion/', views.construccion , name='construccion'),
    path('consumibles/', views.consumibles , name='consumibles'),
    
]
