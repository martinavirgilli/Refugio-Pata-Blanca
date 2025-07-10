from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError

# Create your models here.

class Candidato(models.Model):
    estados = [
        ('disponible', 'Disponible'),
        ('adoptado', 'Adoptado'),
        ('en_proceso', 'En proceso de adopción'),
    ]
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)  # perro, gato, etc.
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    descripcion = models.TextField()
    estado = models.CharField(max_length=50, choices=estados, default="disponible")

    def __str__(self):
        return f"{self.nombre} ({self.tipo})"


class FormularioAdopcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='formularios')
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, related_name='formularios')
    fecha_solicitud = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], default='pendiente')
    comentarios = models.TextField(blank=True)

    def __str__(self):
        return f"Formulario de {self.usuario.username} para {self.candidato.nombre}"


class Visita(models.Model):
    formulario = models.OneToOneField(FormularioAdopcion, on_delete=models.CASCADE, related_name='visita')
    fecha_visita = models.DateField()
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Visita para {self.formulario.candidato.nombre} - {self.fecha_visita}"

    def clean(self):
        # Validación para que la fecha de visita no sea pasada
        if self.fecha_visita < timezone.now().date():
            raise ValidationError("La fecha de visita no puede ser en el pasado.")
        

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()

    def __str__(self):
        return f"{self.user.username}"
