from django.contrib import admin
from .models import Candidato, FormularioAdopcion, Visita, Usuario

# Register your models here.

admin.site.register(Candidato)
admin.site.register(FormularioAdopcion)
admin.site.register(Visita)
admin.site.register(Usuario)