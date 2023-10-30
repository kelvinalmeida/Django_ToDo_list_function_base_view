
from django.urls import path
from .views import home, createToDo

urlpatterns = [
     path('', home, name='home'),
     path('create/', createToDo, name='create'),
]