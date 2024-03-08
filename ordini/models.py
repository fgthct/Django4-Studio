from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.urls import reverse
from anagrafiche.models import Prodotti


# Create your models here.
class Testata_Ordine(models.Model):
    class stato_ordine(models.TextChoices):
        EVASO = "EV", _("Evaso")
        NON_EVASO = "NON_EVA", _("Non Evaso")
        CANCELLATO = "CANC", _("Cancellato")

    cliente = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
    num_ordine = models.SmallIntegerField()
    data_ordine = models.DateTimeField(auto_now_add=True)
    modificato = models.DateField(auto_now=True)
    stato = models.CharField(
        max_length=10, choices=stato_ordine.choices, default=stato_ordine.NON_EVASO
    )

    class Meta:
        verbose_name_plural = "Testate Ordini"

    def __str__(self):
        return f"Ordine nr: {self.num_ordine} - del {self.get_formatted_date()}"

    def get_formatted_date(self):
        return self.data_ordine.strftime("%d-%m-%Y")

    def calcola_totale(self):
        return sum(line.totale for line in self.righe_ordine.all())

    def get_absolute_url(self):
        return reverse("riga_ordine", kwargs={"pk": self.pk})


class Riga_ordine(models.Model):
    ordine = models.ForeignKey(
        Testata_Ordine, related_name="righe_ordine", on_delete=models.CASCADE
    )
    prodotto = models.ForeignKey(Prodotti, on_delete=models.CASCADE)
    quantita = models.IntegerField()
    prezzo = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def totale(self):
        return self.quantita * self.prezzo

    def totale_riga(self):
        return self.quantita * self.prezzo

    def __str__(self):
        return f"Articolo: {self.ordine} - {self.prodotto}"

    class Meta:
        verbose_name_plural = "Righe Ordini"
