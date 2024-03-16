# import unittest
from django.test import TestCase
from .models import Prodotti

#
from django.urls import reverse
from django.shortcuts import render

from anagrafiche.forms import ProdottiForm


class ProdottiTestCase(TestCase):

    def setUp(self):
        Prodotti.objects.create(
            magazzino="Magazzino1",
            articolo="1234567890123",
            descrizione="Descrizione articolo 1",
            qta_iniziale=10,
            quantita=5,
            costo=10.50,
        )
        Prodotti.objects.create(
            magazzino="Magazzino2",
            articolo="9876543210987",
            descrizione="Descrizione articolo 2",
            qta_iniziale=20,
            quantita=15,
            costo=5.75,
        )

    def test_costo_articolo(self):
        prodotto1 = Prodotti.objects.get(articolo="9876543210987")
        self.assertEqual(prodotto1.costo_articolo, 86.25)

    def test_totale_magazzino(self):
        prodotto2 = Prodotti.objects.get(articolo="9876543210987")
        self.assertEqual(prodotto2.totale_magazzino, 172.50)

    def test_valore_magazzino(self):
        self.assertEqual(Prodotti.valore_magazzino(), 138.75)

    def test_str_method(self):
        prodotto1 = Prodotti.objects.get(articolo="9876543210987")
        self.assertEqual(
            str(prodotto1), "Magazzino Magazzino2 - 9876543210987 - Descrizion"
        )


#


class ProdottiViewsTest(TestCase):

    def test_inserisci_prodotto_view(self):
        response = self.client.get(reverse("inserisci_prodotto"))
        self.assertEqual(response.status_code, 200)

    def test_visualizza_prodotti_view(self):
        response = self.client.get(reverse("prodotti"))
        self.assertEqual(response.status_code, 200)

    def test_dettaglio_prodotto_view(self):
        prodotto = Prodotti.objects.create(
            articolo="Prodotto Test",
            costo=10.0,
            qta_iniziale=20,
            quantita=15,
        )  # Create a sample product for testing
        response = self.client.get(
            reverse("dettaglio_prodotto", kwargs={"pk": prodotto.pk})
        )
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_chi_siamo_view(self):
        response = self.client.get(reverse("chi_siamo"))
        self.assertEqual(response.status_code, 200)
