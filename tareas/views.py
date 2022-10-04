from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):

    if request.method == 'GET':
        return render(request, "signup.html", {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado satisfactoriamente')
            except:
                return render(request, "signup.html", {
                    'form': UserCreationForm,
                    "error": 'El ususrio ya existe'
                })

        return render(request, "signup.html", {
            'form': UserCreationForm,
            'error': "Las contraseñas no coinciden"
        })
