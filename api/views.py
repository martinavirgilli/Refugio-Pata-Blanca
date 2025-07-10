from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, serializers, viewsets
from django.contrib.auth.models import User
from .models import Candidato, FormularioAdopcion, Visita, Usuario
from .serializers import CandidatoSerializer, FormularioAdopcionSerializer, VisitaSerializer, UsuarioSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from utils.pagination import CustomPagination
from utils.permission import TienePermisoModelo


# Create your views here.

def inicio(request):
    """Mensaje de bienvenida a la API de Refugio Pata Blanca."""
    return HttpResponse("<h1>Bienvenido a la API de Refugio Pata Blanca.</h1>")

class CandidatoViewSet(viewsets.ModelViewSet):
    queryset = Candidato.objects.all()
    serializer_class = CandidatoSerializer
    permission_classes = [TienePermisoModelo]  # ver sin login pero crear solo con login
    pagination_class = CustomPagination
    model = Candidato

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdminUser()]
        return [IsAuthenticatedOrReadOnly()]

    def get_queryset(self):
        return Candidato.objects.filter(estado='disponible') #solo ver candidatos disponibles


class FormularioAdopcionViewSet(viewsets.ModelViewSet):
    queryset = FormularioAdopcion.objects.all()
    serializer_class = FormularioAdopcionSerializer
    permission_classes = [TienePermisoModelo]
    pagination_class = CustomPagination
    model = FormularioAdopcion

    def get_queryset(self):
        # Si es admin, ve todo
        if self.request.user.is_staff:
            return FormularioAdopcion.objects.all()
        # Si no, solo los suyos
        return FormularioAdopcion.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        usuario = self.request.user
        candidato = serializer.validated_data['candidato']

        # verificar si ya existe un formulario de este usuario para este candidato, si existe no puede mandar otro mas
        if FormularioAdopcion.objects.filter(usuario=usuario, candidato=candidato).exists():
            raise serializers.ValidationError("Ya enviaste un formulario para este candidato.")
        serializer.save(usuario=self.request.user)  # Se asigna automaticamente el usuario autenticado


class VisitaViewSet(viewsets.ModelViewSet):
    queryset = Visita.objects.all()
    serializer_class = VisitaSerializer
    permission_classes = [TienePermisoModelo]
    pagination_class = CustomPagination
    model = Visita

    #validar que solo pueda agendarse una visita si hay un form de adopcion aprobado
    def perform_create(self, serializer):
        formulario = serializer.validated_data['formulario']
        if formulario.estado != 'aprobado':
            raise serializers.ValidationError("Solo se puede agendar una visita si el formulario fue aprobado.")
        serializer.save()

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [TienePermisoModelo]
    pagination_class = CustomPagination
    model = Usuario