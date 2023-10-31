
from django.urls import path
from .views import home, createToDo, deleteToDo, updateToDo, readToDo

urlpatterns = [
     path('', home, name='home'),
     path('create/', createToDo, name='create'),
     path('update/<int:id>', updateToDo, name='update'),
     path('delete/<int:id>', deleteToDo, name='delete'),
     path('read/<int:id>', readToDo, name='read'),
]