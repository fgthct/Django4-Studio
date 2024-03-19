from django import forms
from .models import Corriere

class NuovaConsegnaForm(forms.Form):
    destinatario = forms.CharField(max_length=100)
    indirizzo_destinazione = forms.CharField(max_length=200)
    corriere = forms.ModelChoiceField(queryset=Corriere.objects.all())
    