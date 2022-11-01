from dataclasses import fields
import imp
from django.forms import ModelForm
from django import forms
from dosen.models import Dosen

class FormDosen (ModelForm):
    class Meta:
        model = Dosen
        fields = ['no','nip', 'nama', 'jabatan', 'fakultas', 'email', 'foto']

    widgets = {
        'no' : forms.NumberInput({'class': 'form-control'}),
        'nip' : forms.NumberInput({'class': 'form-control'}),
        'nama' : forms.TextInput({'class': 'form-control'}),
        'jabatan' : forms.TextInput({'class': 'form-control'}),
        'fakultas' : forms.TextInput({'class': 'form-control'}),
        'email' : forms.TextInput({'class': 'form-control'}),
        'foto' : forms.TextInput({'class': 'form-control'}),
    }