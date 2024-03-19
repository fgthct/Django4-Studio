# consegne/models.py
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Corriere(models.Model):
    nome = models.CharField(max_length=100)
    posizione_attuale = models.PointField(
        default=Point(15.0873, 37.5021)
    )  # Catania, Sicilia, Italia

    class Meta:
        verbose_name_plural = "Corrieri"

    def __str__(self):
        return self.nome


class Consegna(models.Model):
    destinatario = models.CharField(max_length=100)
    indirizzo_destinazione = models.CharField(max_length=200)
    corriere = models.ForeignKey(Corriere, on_delete=models.CASCADE)
    completata = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Consegne"

    def __str__(self) -> str:
        return f"Consegna per {self.destinatario} (Corriere: {self.corriere.nome})"
