from django.urls import path
from ordini.views import OrdiniListView, dettaglio_ordine, inserisci_ordine

urlpatterns = [
    path("inserisci_ordine/", inserisci_ordine, name="inserisci_ordine"),
    path("", OrdiniListView.as_view(), name="ordini"),
    path("ordini/<int:pk>/", dettaglio_ordine, name="dettaglio_ordine"),
]
