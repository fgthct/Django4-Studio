from django.urls import path
from . import views

urlpatterns = [
    # path(
    #    "accetta_consegna/<int:consegna_id/",
    #    views.accetta_consegna,
    #    name="accetta_consegna",
    # ),
    path(
        "elenco_nuove_consegne/",
        views.elenco_nuove_consegne,
        name="elenco_nuove_consegne",
    ),
    path("elenco_corrieri/", views.elenco_corrieri, name="elenco_corrieri"),
    path("elenco_consegne/", views.elenco_consegne, name="elenco_consegne"),
    path("consegne_fatte/", views.elenco_consegne_completate, name="consegne_fatte"),
    path("nuova_consegna/", views.nuova_consegna, name="nuova_consegna"),
    # path("aggiorna_posizione_corriere/<int:corriere_id>/",
    #    views.aggiorna_posizione_corriere,
    #    name="aggiorna_posizione_corriere",
    # ),
    # Altri percorsi per le tue altre viste...
]
