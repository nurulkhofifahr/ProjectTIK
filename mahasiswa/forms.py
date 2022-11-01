from dataclasses import fields
import imp
from django.forms import ModelForm
from django import forms
from mahasiswa.models import Mahasiswa

class FormMahasiswa (ModelForm):
    class Meta:
        model = Mahasiswa
        fields = ['no','nim', 'nama', 'ttl', 'email', 'foto']

    widgets = {
        'no' : forms.NumberInput({'class': 'form-control'}),
        'nim' : forms.NumberInput({'class': 'form-control'}),
        'nama' : forms.TextInput({'class': 'form-control'}),
        'ttl' : forms.TextInput({'class': 'form-control'}),
        'email' : forms.TextInput({'class': 'form-control'}),
        'foto' : forms.TextInput({'class': 'form-control'}),
    }