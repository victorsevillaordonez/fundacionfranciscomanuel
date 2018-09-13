from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Galeria,Usuario,Evento

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class GaleriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Galeria
        fields = '__all__'
class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'