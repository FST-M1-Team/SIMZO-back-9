from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Une petite vue simple pour l'accueil
def home(request):
    return HttpResponse("<h1>Bienvenue sur SIMZO !</h1><p>Le serveur fonctionne.</p>")

urlpatterns = [
    path('', home),  # La racine (http://127.0.0.1)
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
]
