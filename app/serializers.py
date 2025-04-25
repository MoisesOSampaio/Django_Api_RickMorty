from rest_framework import serializers
from .models import Personagens

class PersonagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personagens
        fields = '__all__'