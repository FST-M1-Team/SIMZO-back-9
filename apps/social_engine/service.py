import requests
from django.conf import settings

def get_meta_data():
    """
    Récupère les informations de base du compte Meta (Facebook/Instagram).
    """
    api_key = getattr(settings, 'META_API_KEY', None)
    
    if not api_key:
        return {"error": "La clé META_API_KEY n'est pas configurée."}

    # L'URL correcte de l'API Graph de Meta
    url = f"https://graph.facebook.com{api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Génère une erreur si l'appel échoue
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
