#encoding:utf-8
from django import forms

class BuscarPorTituloForm(forms.Form):
    titulo = forms.CharField(label='Titulo del album', widget=forms.TextInput, required=True)
    
class BuscarPorFechaForm(forms.Form):
    fecha = forms.DateField(label='Fecha de lanzamiento', widget=forms.TextInput, required=True)