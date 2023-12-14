from django import forms
from .models import FormModel
from django.forms import Select, TextInput, Textarea
# Create your form here.

base = TextInput(attrs={'class': "form-control w-96"})
choice = Select(attrs={'class': 'ratio flex  w-96 flex-row'})
text_field = Textarea(attrs={'class': "form-control w-96 h-300"})

class Form(forms.ModelForm):
    class Meta:
        model = FormModel
        fields = '__all__'
        widgets = {
            'name': base,
            'Nausea': choice,
            'Desconforto Estomacal': choice,
            'Desconforto': choice,
            'Descrição': text_field,
        }
