from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf import settings  
from django.conf.urls.static import static
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
#  vue pour l'accueil
def home(request):
    return HttpResponse("<h1>Bienvenue sur SIMZO !</h1><p>Le serveur fonctionne.</p>")

urlpatterns = [
    path('', home),  # La racine (http://127.0.0.1)
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.v1.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Auth pour l'interface de navigation DRF
    path('api-auth/', include('rest_framework.urls')),

]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

