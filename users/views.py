# -*- coding: utf-8 -*-
import logging
from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.shortcuts import render, redirect
from users.forms import LoginForm

logger = logging.getLogger(__name__)

def login(request):
    error_messages = []
    if request.method == 'POST':
        # Using form instade of direct request.POST
        # username = request.POST.get('usr', '')
        # password = request.POST.get('pwd', '')
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')

            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o clave incorrectos')
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next','photos_home'))
                else:
                    error_messages.append('El usuario no esta activo')
    else:
        form = LoginForm()

    context = {
        'errors':error_messages,
        'login_form':form
    }
    return render(request, 'users/login.html', context)

def logout(request):
    django_logout(request)
    return redirect('photos_home')

def prueba(req):
    context = dict(myvar='hola')
    return render(req, 'users/prueba.html', context)


