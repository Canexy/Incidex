from django.apps import AppConfig
from django.db.models.signals import post_migrate, m2m_changed


def crear_grupos(sender, **kwargs):
    from django.contrib.auth.models import Group

    for nombre in ['Usuarios', 'Técnicos', 'Administrador']:
        Group.objects.get_or_create(name=nombre)


def sincronizar_tecnico(sender, instance, action, pk_set, **kwargs):
    from django.contrib.auth.models import Group
    from .models import Especialidad

    try:
        grupo_tecnicos = Group.objects.get(name='Técnicos')
    except Group.DoesNotExist:
        return

    if action == 'post_add' and grupo_tecnicos.pk in pk_set:
        Especialidad.objects.get_or_create(usuario=instance)

    if action == 'post_remove' and grupo_tecnicos.pk in pk_set:
        Especialidad.objects.filter(usuario=instance).delete()


class IncidenciasConfig(AppConfig):
    name = 'incidencias'

    def ready(self):
        from django.contrib.auth.models import User

        post_migrate.connect(crear_grupos, sender=self)
        m2m_changed.connect(
            sincronizar_tecnico,
            sender=User.groups.through
        )
