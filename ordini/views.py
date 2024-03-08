from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404

from ordini.models import Testata_Ordine, Riga_ordine
from ordini.forms import OrdineForm, RigaOrdineForm
from .forms import RigaOrdineFormSet
from django.forms import inlineformset_factory
from anagrafiche.models import Prodotti  # Importa il modello dei prodotti


# inserimento ordini
def inserisci_ordine(request):
    RigaOrdineFormSet = inlineformset_factory(
        Testata_Ordine, Riga_ordine, form=RigaOrdineForm, extra=3
    )

    if request.method == "POST":
        ordine_form = OrdineForm(request.POST)
        righe_formset = RigaOrdineFormSet(request.POST)

        if ordine_form.is_valid() and righe_formset.is_valid():
            ordine = ordine_form.save(commit=False)
            righe_formset.instance = ordine
            ordine.save()
            righe_formset.save()
            # Decrementa la quantità nell'anagrafica dei prodotti
            for riga_form in righe_formset:
                if "prodotto" in riga_form.cleaned_data:
                    prodotto = riga_form.cleaned_data["prodotto"]
                    quantita = riga_form.cleaned_data["quantita"]
                    prodotto.quantita -= quantita
                    prodotto.save()
            return redirect("dettaglio_ordine", pk=ordine.pk)
    else:
        ordine_form = OrdineForm()
        righe_formset = RigaOrdineFormSet()

    return render(
        request,
        "ordini/inserisci_ordine.html",
        {"ordine_form": ordine_form, "righe_formset": righe_formset},
    )


# Create your views here.
def dettaglio_ordine(request, pk):
    ordine = Testata_Ordine.objects.get(pk=pk)
    totale_ordine = sum(riga.totale_riga() for riga in ordine.righe_ordine.all())
    return render(
        request,
        "ordini/dettaglio_ordini.html",
        {"ordine": ordine, "totale_ordine": totale_ordine},
    )


class OrdiniListView(ListView):
    model = Testata_Ordine
    context_object_name = "lista_ordini"
    template_name = "ordini/ordini.html"


class RigheListView(DetailView):
    model = Riga_ordine
    context_object_name = "Righe_ordine"
    template_name = "ordini/dettaglio_ordini.html"
