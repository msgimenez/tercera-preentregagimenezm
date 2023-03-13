from django import forms


class pelisformulario(forms.Form):
    titulo = forms.CharField()
    genero =forms.CharField()
    director =forms.CharField()
 