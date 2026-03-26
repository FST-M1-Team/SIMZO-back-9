from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import AnnonceurProfile, InfluenceurProfile # Importez vos modèles

User = get_user_model()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # On vérifie le rôle pour créer le bon profil
        if instance.role == 'ANNONCEUR':
            AnnonceurProfile.objects.create(user=instance)
        elif instance.role == 'INFLUENCEUR':
            InfluenceurProfile.objects.create(user=instance)
