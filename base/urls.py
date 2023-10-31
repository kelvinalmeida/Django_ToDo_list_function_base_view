
from django.urls import path
from .views import home, createToDo, deleteToDo, updateToDo

urlpatterns = [
     path('', home, name='home'),
     path('create/', createToDo, name='create'),
     path('update/<int:id>', updateToDo, name='update'),
     path('delete/<int:id>', deleteToDo, name='delete'),
]