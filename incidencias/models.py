from django.db import models
from django.contrib.auth.models import User

class Tecnico(models.Model):

    ESPECIALIDAD_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
    ]

    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='tecnico'
    )
    especialidad = models.CharField(
        max_length=20,
        choices=ESPECIALIDAD_CHOICES
    )

    def __str__(self):
        return f"{self.usuario.username} ({self.especialidad})"

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

    criticidad = models.CharField(
        max_length=10,
        choices=CRITICIDAD_CHOICES
    )

    tipo_incidencia = models.CharField(
        max_length=10,
        choices=TIPO_INCIDENCIA_CHOICES
    )

    estado = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='nuevo'
    )

    fecha_creacion = models.DateTimeField(auto_now_add=True)

    usuario_creador = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='incidencias'
    )

    tecnico_asignado = models.ForeignKey(
        Tecnico,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='incidencias'
    )

    def __str__(self):
        return f"[{self.estado}] {self.titulo}"
