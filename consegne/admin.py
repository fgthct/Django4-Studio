from django.contrib.gis import admin

from leaflet.admin import LeafletGeoAdmin

from consegne.models import Consegna, Corriere


@admin.register(Corriere)
class CorriereAdmin(LeafletGeoAdmin):
    list_display = ("nome", "posizione_attuale")


# Register your models here.
admin.site.register(Consegna)
