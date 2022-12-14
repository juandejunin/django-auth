
from multiprocessing import AuthenticationError
from types import NoneType
from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError

from .form import TaskCreate
#importar el modelo de las tareas
from .models import Task


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })

    else:
        # Comprobar si las contraseñas coinciden
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                # Guardar en la base de datos
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Una vez que se guarde el usuario vamos a ejecutar login, se pasan dos parametros, el primeo es request y el segundo es el usuario que queremos guardar
                login(request, user)
                # Redireccionar a una pagina nueva
                return redirect('tasks')
            except IntegrityError:

                # Si el usuario elegido ya existe
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    "error": 'El ususrio ya existe'
                })

        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })


def tasks(request):
    #obteniendo todas las tareas que estan en la base de datos
    tasks =  Task.objects.filter(user=request.user, dateCompleted__isnull=True)
    return render(request, 'tasks.html', {'tasks':tasks})


def create_task(request):

    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskCreate
        })
    else:
        try:
            # print(request.POST)
            # cuando el metodo sea post yo voy  a llamar a TaskCreate y le paso el request.POST
            form = TaskCreate(request.POST)
        # esto genera un formulario
        # print(form)
            nueva_tarea = form.save(commit=False)
            nueva_tarea.user = request.user
        # print(nueva_tarea)
            nueva_tarea.save()

            return redirect('tasks')

        except ValueError:
            return render (request,'create_task.html',{
                'form': TaskCreate,
                'error': 'Por favor ingresa datos validos'
            })


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password']
                            )
        # print(request.POST)
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'El usuario o la contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect('tasks')
