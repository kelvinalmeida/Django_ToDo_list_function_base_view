from django.shortcuts import render
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

    context = {
        "form": form,
    }
    return render(request, 'base/create.html', context)