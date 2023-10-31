from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .form import CrateForm
from .models import ToDo


# Create your views here.


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