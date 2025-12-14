from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import Incidencia, Tecnico


@login_required
def home(request):
    user = request.user
    context = {}

    # Usuario normal
    if user.groups.filter(name='Usuarios').exists():
        incidencias = Incidencia.objects.filter(usuario_creador=user)
        context['tipo_panel'] = 'usuario'
        context['incidencias'] = incidencias

    # Técnico
    elif user.groups.filter(name='Técnicos').exists():
        try:
            tecnico = user.tecnico
        except Tecnico.DoesNotExist:
            tecnico = None

        if tecnico:
            incidencias_disponibles = Incidencia.objects.filter(
                tipo_incidencia=tecnico.especialidad,
                tecnico_asignado__isnull=True
            )

            incidencias_asignadas = Incidencia.objects.filter(
                tecnico_asignado=tecnico
            )

            context['tipo_panel'] = 'tecnico'
            context['incidencias_disponibles'] = incidencias_disponibles
            context['incidencias_asignadas'] = incidencias_asignadas
        else:
            context['tipo_panel'] = 'tecnico_sin_perfil'

    # Administrador (o cualquier otro caso raro)
    else:
        incidencias = Incidencia.objects.all()
        context['tipo_panel'] = 'admin'
        context['incidencias'] = incidencias

    return render(request, "incidencias/home.html", context)
