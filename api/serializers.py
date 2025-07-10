from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Candidato, FormularioAdopcion, Visita, Usuario

class CandidatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidato
        fields = '__all__'

class FormularioAdopcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormularioAdopcion
        fields = '__all__'
        read_only_fields = ['usuario']  # El usuario se toma automaticamente de quien está creando el formulario


class VisitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visita
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
    