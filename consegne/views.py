# consegne/views.py
from django.shortcuts import render
from django.contrib.gis.geos import Point
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Corriere, Consegna
from .forms import NuovaConsegnaForm


def elenco_consegne(request):
    consegne = Consegna.objects.all()
    return render(request, "consegne/elenco_consegne.html", {"consegne": consegne})


def elenco_nuove_consegne(request):
    nuove_consegne = Consegna.objects.filter(completata=False)
    context = {"nuove_consegne": nuove_consegne}
    return render(request, "consegne/elenco_nuove_consegne.html", context)


def elenco_consegne_completate(request):
    consegne_fatte = Consegna.objects.filter(completata=True)
    context = {"consegne_fatte": consegne_fatte}
    return render(request, "consegne/elenco_consegne_fatte.html", context)


""" def accetta_consegna(request, consegna_id):
    consegna = Consegna.objects.get(id=consegna_id)
    print(consegna_id)
    consegna.completata = True
    consegna.save()
    return redirect("elenco_nuove_consegne") """


def nuova_consegna(request):
    if request.method == "POST":
        form = NuovaConsegnaForm(request.POST)
        if form.is_valid():
            # Recupera i dati dal form
            destinatario = form.cleaned_data["destinatario"]
            indirizzo_destinazione = form.cleaned_data["indirizzo_destinazione"]
            corriere = form.cleaned_data["corriere"]

            # Crea una nuova Consegna
            consegna = Consegna.objects.create(
                destinatario=destinatario,
                indirizzo_destinazione=indirizzo_destinazione,
                corriere=corriere,
            )
            print(f"Nuova consegna creata: {consegna}")

            # Redirige l'utente all'elenco delle nuove consegne
            return redirect("elenco_nuove_consegne")
    else:
        form = NuovaConsegnaForm()

    return render(request, "consegne/nuova_consegna.html", {"form": form})


def completa_consegna(request, consegna_id):
    consegna = Consegna.objects.get(id=consegna_id)
    consegna.completata = True
    consegna.save()
    return redirect("elenco_consegne")


import json


def elenco_corrieri(request):
    corrieri = Corriere.objects.all()
    corrieri_data = json.dumps(
        [
            {
                "nome": corriere.nome,
                "posizione_attuale": {
                    "x": corriere.posizione_attuale.x,
                    "y": corriere.posizione_attuale.y,
                },
            }
            for corriere in corrieri
        ]
    )
    return render(
        request,
        "consegne/elenco_corrieri.html",
        {"corrieri": corrieri, "corrieri_data": corrieri_data},
    )




def aggiorna_posizione_corriere(request, corriere_id):
    corriere = get_object_or_404(Corriere, pk=corriere_id)

    if request.method == "POST":
        latitudine = request.POST.get("latitudine")
        longitudine = request.POST.get("longitudine")

        if latitudine is not None and longitudine is not None:
            # Aggiorna la posizione attuale del corriere
            corriere.posizione_attuale = Point(float(longitudine), float(latitudine))
            corriere.save()

            # Restituisci una risposta JSON di successo
            return JsonResponse({"success": True})
        else:
            # Restituisci una risposta JSON di errore se latitudine e/o longitudine sono mancanti
            return JsonResponse(
                {"error": "Latitudine e/o longitudine mancanti"}, status=400
            )

    # Restituisci una risposta JSON di errore se la richiesta non è di tipo POST
    return JsonResponse({"error": "Richiesta non consentita"}, status=405)
