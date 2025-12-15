from django.db import models
from django.contrib.auth.models import User

# Extensión del modelo User.
class Tecnico(models.Model):
    ESPECIALIDAD_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
    ]

    # Un técnico es un usuario. Un usuario puede ser técnico o no.
    # Si se elimina al usuario, se elimina también al técnico.
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='tecnico')
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDAD_CHOICES)

    def __str__(self):
        return f"{self.usuario.username} ({self.get_especialidad_display()})"

class Incidencia(models.Model):
    CRITICIDAD_CHOICES = [
        ('bajo', 'Bajo'),
        ('medio', 'Medio'),
        ('alto', 'Alto'),
        ('critico', 'Crítico'),
    ]

    TIPO_INCIDENCIA_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
    ]

    ESTADO_CHOICES = [
        ('nuevo', 'Nuevo'),
        ('abierto', 'Abierto'),
        ('pendiente', 'Pendiente'),
        ('en_espera', 'En Espera'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]

    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    criticidad = models.CharField(max_length=10, choices=CRITICIDAD_CHOICES)
    tipo_incidencia = models.CharField(max_length=10, choices=TIPO_INCIDENCIA_CHOICES)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='nuevo')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    # Si se borra el usuario creador, se eliminan sus incidencias.
    usuario_creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incidencias')
    # Una incidencia puede no tener técnico asignado. Si lo tiene, es un técnico existente. Si el técnico se elimina, la incidencia queda sin técnico asignado (null).
    tecnico_asignado = models.ForeignKey(Tecnico, on_delete=models.SET_NULL, null=True, blank=True, related_name='incidencias')

    def __str__(self):
        return f"[{self.get_estado_display()}] {self.titulo}"

# Historial de cambios de estado de una incidencia.
class HistorialEstadoIncidencia(models.Model):
    # Si se borra la incidencia, se eliminan sus historial de estados.
    incidencia = models.ForeignKey(Incidencia, on_delete=models.CASCADE, related_name='historial_estados')
    estado_anterior = models.CharField(max_length=20)
    estado_nuevo = models.CharField(max_length=20)
    # Si el técnico que hizo el cambio se elimina, se deja como null.
    cambiado_por = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_cambio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Incidencia {self.incidencia.id}: "
            f"{self.estado_anterior} → {self.estado_nuevo}"
        )
