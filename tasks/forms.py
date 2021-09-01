from django import forms
from django.forms import ModelForm, fields

from .models import *
from .forms import *


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = '__all__'