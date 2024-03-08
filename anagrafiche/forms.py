from django import forms
from .models import Prodotti


class ProdottiForm(forms.ModelForm):
    class Meta:
        model = Prodotti
        fields = [
            "magazzino",
            "articolo",
            "descrizione",
            "foto",
            "qta_iniziale",
            "quantita",
            "costo",
        ]
