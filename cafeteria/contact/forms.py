import email
from unicodedata import name
from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Nombre', required=True, max_length=100, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu nombre'
        }
    ))
    email = forms.EmailField(label='Email', required=True, widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Escribe tu email'
        }
    ))
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Escribe tu mensaje'
        }
    ))
