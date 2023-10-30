from django.forms import forms, ModelForm
from .models import ToDo


class CrateForm(ModelForm):

    class Meta:
        model = ToDo
        fields = '__all__'