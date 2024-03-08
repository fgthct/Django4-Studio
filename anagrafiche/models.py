from django.db import models
from django.urls import reverse


class Prodotti(models.Model):
    magazzino = models.CharField(max_length=50)
    articolo = models.CharField(max_length=13)
    descrizione = models.CharField(max_length=250)
    foto = models.ImageField(upload_to="foto_articoli", blank=True, null=True)
    qta_iniziale = models.IntegerField()
    quantita = models.IntegerField()
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = "Prodotti"

    def get_absolute_url(self):
        return reverse("dettaglio_prodotto", kwargs={"pk": self.pk})

    @property
    def costo_articolo(self):
        return self.quantita * self.costo

    @property
    def totale_magazzino(self):
        tot_articoli = Prodotti.objects.count() * self.costo_articolo
        return tot_articoli

    @staticmethod
    def valore_magazzino():
        totale_magazzino = 0
        for prodotto in Prodotti.objects.all():
            totale_magazzino += prodotto.costo_articolo
        return totale_magazzino

    def __str__(self) -> str:
        return f"Magazzino {self.magazzino} - {self.articolo} - {self.descrizione[:10]}"
