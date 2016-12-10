from django import forms
from django.forms import ModelForm
from .models import Director


class DirectorCreationForm(ModelForm):
    class Meta:
        model = Director
        fields = ['name', 'surname', 'avatar', 'birthdate', 'year', 'score', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'pattern': '^([A-Z]{1}[a-z]*)$'}),
            'surname': forms.TextInput(attrs={'pattern': '^([A-Z]{1}[a-z]*)$'}),
            'birthdate': forms.TextInput(attrs={'pattern': '^(\d{4}-\d{2}-\d{2})$'}),
            'year': forms.TextInput(attrs={'pattern': '^(\d{4})$', 'type': 'number'}),
            'score': forms.TextInput(attrs={'pattern': '^(\d+(\.\d{1,2}){0,1})$', 'type': 'number', 'min': '1', 'step': '0.01'}),
            'email': forms.TextInput(attrs={'pattern': '^(\w+@([a-z]+)\.[.a-z]+)$', 'type': 'email'})
        }


class DirectorSearchForm(forms.Form):
    name = forms.CharField(max_length=20)
