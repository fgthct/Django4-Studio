from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from anagrafiche.views import home, chi_siamo

urlpatterns = [
    path("", home, name="home"),
    path("chi_siamo/", chi_siamo, name="chi_siamo"),
    path("prodotti/", include("anagrafiche.urls"), name="anagrafiche"),
    path("ordini/", include("ordini.urls"), name="ordini"),
    path("admin/", admin.site.urls),
]
# Configurazione delle URL per i file statici in modalità di sviluppo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
