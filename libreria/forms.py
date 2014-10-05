# -*- encoding: utf-8 -*-

from django import forms
from libreria.models import Autor, Genero, Estanteria, Libro, UserProfile
from django.contrib.auth.models import User
import datetime

class crear_autor_form(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Nombre: ")
    apellidos = forms.CharField(max_length=128, help_text="Apellidos: ")
    fecha_nacimiento = forms.DateField(initial=datetime.date.today, input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'), help_text="Fecha de nacimiento: ")

    class Meta:
        model = Autor


class crear_genero_form(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Nombre: ")

    class Meta:
        model = Genero


class crear_estanteria_form(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Nombre: ")

    class Meta:
        model = Estanteria


class crear_libro_form(forms.ModelForm):
    nombre = forms.CharField(max_length=128, help_text="Nombre: ")
    fecha_publicacion = forms.DateField(initial=datetime.date.today, input_formats=['%d/%m/%Y'], widget=forms.DateInput(format='%d/%m/%Y'), help_text="Fecha: ")
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), help_text="Autor: ")
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), help_text="Género: ")
    estanteria = forms.ModelChoiceField(queryset=Estanteria.objects.all(), help_text="Estantería: ")
    class Meta:
        model = Libro


class registro_form(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')