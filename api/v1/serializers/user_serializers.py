from rest_framework import serializers
from apps.users.models import User # Chemin explicite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
