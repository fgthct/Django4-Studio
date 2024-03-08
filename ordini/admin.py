""" from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from ordini.models import Testata_Ordine


class TestataOrdineAdmin(admin.ModelAdmin):
    list_display = ("num_ordine", "cliente", "data_ordine", "link_righe_ordine")

    def link_righe_ordine(self, obj):
        url = (
            reverse("admin:ordini_rigaordine_changelist")
            + f"?order__id__exact={obj.id}"
        )
        return format_html('<a href="{}">Righe Ordine</a>', url)

    link_righe_ordine.short_description = "Righe Ordine"


admin.site.register(Testata_Ordine, TestataOrdineAdmin) """

####
from django.contrib import admin
from ordini.models import Testata_Ordine, Riga_ordine


# Register your models here.
class TestataOrdineAdmin(admin.ModelAdmin):
    list_display = ("cliente", "num_ordine", "data_ordine")


admin.site.register(Testata_Ordine, TestataOrdineAdmin)


class RigaOrdineAdmin(admin.ModelAdmin):
    list_display = ("ordine", "prodotto", "quantita")


admin.site.register(Riga_ordine, RigaOrdineAdmin)
