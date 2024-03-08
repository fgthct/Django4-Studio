from django import forms
from ordini.models import Testata_Ordine, Riga_ordine
from django.forms import modelformset_factory
from anagrafiche.models import Prodotti


class OrdineForm(forms.ModelForm):
    class Meta:
        model = Testata_Ordine
        fields = ["cliente", "num_ordine", "stato"]
        verbose_name_plural = "Testate Ordini"


class RigaOrdineForm(forms.ModelForm):
    class Meta:
        model = Riga_ordine
        fields = ["prodotto", "quantita", "prezzo"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["prodotto"].queryset = (
            Prodotti.objects.all()
        )  # Imposta il queryset per il campo prodotto

    def clean(self):
        cleaned_data = super().clean()
        prodotto = cleaned_data.get("prodotto")
        quantita = cleaned_data.get("quantita")
        if not prodotto:
            raise forms.ValidationError("Il campo prodotto è richiesto.")
        if quantita:
            # Controllo della disponibilità di quantità nel magazzino
            if quantita > prodotto.quantita:
                raise forms.ValidationError("Quantità non disponibile nel magazzino.")
        return cleaned_data


RigaOrdineFormSet = modelformset_factory(Riga_ordine, form=RigaOrdineForm, extra=1)
