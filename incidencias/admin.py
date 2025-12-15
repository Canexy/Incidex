from django.contrib import admin
from .models import Tecnico, Incidencia

# Vistas de administración para los modelos.

@admin.register(Tecnico)
class TecnicoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'especialidad')


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'criticidad', 'tipo_incidencia', 'usuario_creador', 'tecnico_asignado')
    list_filter = ('estado', 'criticidad', 'tipo_incidencia')
    search_fields = ('titulo', 'descripcion')
