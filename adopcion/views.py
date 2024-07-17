from django.shortcuts import render, redirect
from .models import Mascota, Animal
from .forms import  CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout




# Create your views here.
@login_required
def index(request):
    animal = Animal.objects.all()
    data={"animal": animal}
    return render(request,'Menu/index.html',data)

def mascotas(request):
    mascotas = Mascota.objects.all()
    data = {"mascotas" : mascotas} #<- diccionario.
    return render(request, 'menu/carrito.html', data)

def carrito(request):
    return render(request, 'menu/carrito.html')

def signup(request):
    data = {'form' : CustomUserCreationForm()}
    if request.method == "POST":
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            data["mensaje"]="El usuario se a guardado correctamente"
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)

            return redirect('/')
        else:
            data["form"]= user_creation_form

    return render(request, 'menu/registracion/signup.html', data)

def login(request):
    return render(request, 'menu/registracion/login.html')

def exit(request):
    logout(request)
    return redirect('/')



