from django.shortcuts import render
from authapp.forms import ProjektUserLoginForm, ProjektUserRegisterForm, ProjektUserEditForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def login(request):

    login_form = ProjektUserLoginForm (data = request.POST)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
            
    content = {
        'title':'Вход',
        'login_form':login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))

def register(request):
    
    if request.method == 'POST':
        register_form = ProjektUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ProjektUserRegisterForm()

    
    title = 'Регистрация'
    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content)

def edit(request):
    title = 'Редактирование'
    if request.method == 'POST':
        edit_form = ProjektUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ProjektUserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)