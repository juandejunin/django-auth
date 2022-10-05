from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })

    else:
        #Comprobar si las contraseñas coinciden
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                #Guardar en la base de datos
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                #Una vez que se guarde el usuario vamos a ejecutar login, se pasan dos parametros, el primeo es request y el segundo es el usuario que queremos guardar
                login(request, user)
                #Redireccionar a una pagina nueva
                return redirect('tasks')
            except IntegrityError:
                
                #Si el usuario elegido ya existe
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    "error": 'El ususrio ya existe'
                })

        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })

def tasks(request):
    return render (request, 'tasks.html')