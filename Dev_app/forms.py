from django.forms import ModelForm
from django import forms
from .models import Profile


class Profileform(forms.ModelForm):

    last_name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3 ",
        "type": "input",
        "placeholder": "last_name ",
        "id": 'text'
    }), label_suffix='')

    bio = forms.CharField(widget=forms.Textarea(attrs={
        "class": "form-control mb-3 ",
        "type": "input",
        "placeholder": "bio ",
        "id": 'text'
    }), label_suffix='')
    location = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control mb-3 ",
        "type": "input",
        "placeholder": "location ",
        "id": 'text'
    }), label_suffix='')

    img = forms.ImageField(widget=forms.FileInput(attrs={

        "class": "form-control ", }))

    class Meta:
        model = Profile
        fields = ['last_name', 'bio', 'location', 'img']
