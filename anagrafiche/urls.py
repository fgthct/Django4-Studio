from django.urls import path
from anagrafiche import views

urlpatterns = [
    path("", 
         views.visualizza_prodotti, 
         name="prodotti"),
    path('inserisci_articolo/', 
         views.inserisci_prodotto, 
         name='inserisci_prodotto'),
    path("prodotti/<int:pk>/", 
         views.dettaglio_prodotto, 
         name="dettaglio_prodotto"),
]
