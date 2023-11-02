from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .form import CrateForm, LoginForm
from .models import ToDo

from django.contrib.auth import login, authenticate, logout


# Create your views here.
def login_view(request, *args, **kwargs):
    
    form = LoginForm()
    menssagem = ''

    if(request.method == "POST"):
        form = LoginForm(request.POST)
        print('entrei')

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username = username, password = password)
            print(user)

            if user is not None:
                login(request, user)
                print('logou')
                return redirect('home')
            else:
                menssagem = '** usuário não existe'         

    context = {
        "form": form,
        "menssagem": menssagem,
    }

    return render(request, 'base/login.html', context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect('login')


def home(request, *args, **kwargs):
    querySet = ToDo.objects.all()
    # print(querySet)
    context = {
        "to_dos": querySet
    }
    return render(request, 'base/home.html', context)

def createToDo(request, *args, **kwargs):
    form = CrateForm(request.POST)

    if form.is_valid():
        form.save(commit=True) 
        return HttpResponseRedirect(reverse('home'))

    context = {
        "form": form,
    }
    return render(request, 'base/form.html', context)

def updateToDo(request, id, *args, **kwargs):

    to_do = get_object_or_404(ToDo, id=id)

    form = CrateForm(request.POST or None, instance=to_do)

    if form.is_valid():
        form.save(commit=True) 
        return HttpResponseRedirect(reverse('home'))

    context = {
        "form": form,
    }

    return render(request, 'base/form.html', context)

def deleteToDo(request, id, *args, **kwargs):
    print(args)
    print(kwargs)
    
    # id = kwargs['id']
    
    to_do = get_object_or_404(ToDo, id=id)
    
    print(to_do.title)

    if(request.method == 'POST'):
        to_do.delete()
        return HttpResponseRedirect(reverse('home'))

    context = {
        "to_do": to_do
    }

    return render(request, 'base/delete.html', context)

def readToDo(request, id, *args, **kwargs):

    to_do = get_object_or_404(ToDo, id=id)
    
    context = {
        "to_do": to_do
    }

    return render(request, 'base/read.html', context)