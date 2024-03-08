from django.shortcuts import render, redirect
from anagrafiche.models import Prodotti

from anagrafiche.forms import ProdottiForm


# Create
def inserisci_prodotto(request):
    if request.method == "POST":
        form = ProdottiForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProdottiForm()
    context = {"form": form}
    return render(request, "prodotti/inserisci.html", context)


def visualizza_prodotti(request):
    prodotti = Prodotti.objects.all()
    context = {"prodotti": prodotti}
    return render(request, "prodotti/visualizza_prodotti.html", context)


def dettaglio_prodotto(request, pk):
    prodotto = Prodotti.objects.get(id=pk)
    context = {"prodotto": prodotto}
    return render(request, "prodotti/dettaglio_prodotto.html", context)


def home(request):
    return render(request, "home.html")

def chi_siamo(request):
    return render(request, "chi_siamo.html")
