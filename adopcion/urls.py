from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'), #path para el nav-inicio
    path('',views.index,name='index'), #path para el nav-sobre nosotros
    path('mascotas', views.mascotas, name='mascotas'),
    path('carrito', views.carrito, name='carrito'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.exit, name='exit'),
    
    
]