from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST

from .models import Incidencia, Tecnico
from .forms import IncidenciaForm


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

@login_required
@require_POST
def autoasignar_incidencia(request, incidencia_id):
    user = request.user

    # Solo técnicos
    if not user.groups.filter(name='Técnicos').exists():
        return redirect('home')

    try:
        tecnico = user.tecnico
    except:
        return redirect('home')

    incidencia = get_object_or_404(
        Incidencia,
        id=incidencia_id,
        tecnico_asignado__isnull=True,
        tipo_incidencia=tecnico.especialidad
    )

    incidencia.tecnico_asignado = tecnico
    incidencia.estado = 'abierto'
    incidencia.save()

    return redirect('home')

@login_required
@require_POST
def cambiar_estado_incidencia(request, incidencia_id):
    user = request.user

    if not user.groups.filter(name='Técnicos').exists():
        return redirect('home')

    try:
        tecnico = user.tecnico
    except:
        return redirect('home')

    incidencia = get_object_or_404(
        Incidencia,
        id=incidencia_id,
        tecnico_asignado=tecnico
    )

    nuevo_estado = request.POST.get('estado')

    estados_validos = ['pendiente', 'en_espera', 'resuelto', 'cerrado']

    if nuevo_estado in estados_validos:
        incidencia.estado = nuevo_estado
        incidencia.save()

    return redirect('home')

@login_required
def crear_incidencia(request):
    user = request.user

    if not user.groups.filter(name='Usuarios').exists():
        return redirect('home')

    if request.method == 'POST':
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            incidencia = form.save(commit=False)
            incidencia.usuario_creador = user
            incidencia.estado = 'nuevo'
            incidencia.save()
            return redirect('home')
    else:
        form = IncidenciaForm()

    return render(request, 'incidencias/crear_incidencia.html', {'form': form})