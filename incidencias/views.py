from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from .models import Incidencia, Especialidad, HistorialEstadoIncidencia
from .forms import IncidenciaForm


@login_required
def home(request):
    user = request.user
    context = {}

    es_admin = (
        user.is_superuser or
        user.groups.filter(name='Administrador').exists()
    )

    if user.groups.filter(name='Usuarios').exists():
        incidencias_activas = Incidencia.objects.filter(
            usuario_creador=user
        ).exclude(estado='cerrado')

        incidencias_cerradas = Incidencia.objects.filter(
            usuario_creador=user,
            estado='cerrado'
        )

        context['tipo_panel'] = 'usuario'
        context['incidencias'] = incidencias_activas
        context['incidencias_cerradas'] = incidencias_cerradas

    elif user.groups.filter(name='Técnicos').exists():
        try:
            especialidad = user.especialidad
        except Especialidad.DoesNotExist:
            especialidad = None

        if especialidad:
            incidencias_disponibles = Incidencia.objects.filter(
                tipo_incidencia=especialidad.especialidad,
                tecnico_asignado__isnull=True
            )

            incidencias_asignadas = Incidencia.objects.filter(
                tecnico_asignado=especialidad
            ).exclude(estado='cerrado')

            incidencias_cerradas = Incidencia.objects.filter(
                tecnico_asignado=especialidad,
                estado='cerrado'
            )

            context['tipo_panel'] = 'tecnico'
            context['incidencias_disponibles'] = incidencias_disponibles
            context['incidencias_asignadas'] = incidencias_asignadas
            context['incidencias_cerradas'] = incidencias_cerradas
        else:
            context['tipo_panel'] = 'tecnico_sin_perfil'

    elif es_admin:
        incidencias_activas = Incidencia.objects.exclude(estado='cerrado')
        incidencias_cerradas = Incidencia.objects.filter(estado='cerrado')

        context['tipo_panel'] = 'admin'
        context['incidencias'] = incidencias_activas
        context['incidencias_cerradas'] = incidencias_cerradas

    else:
        context['tipo_panel'] = 'sin_permiso'

    return render(request, "incidencias/home.html", context)


@login_required
@require_POST
def autoasignar_incidencia(request, incidencia_id):
    user = request.user

    if not user.groups.filter(name='Técnicos').exists():
        return redirect('home')

    try:
        especialidad = user.especialidad
    except Especialidad.DoesNotExist:
        return redirect('home')

    incidencia = get_object_or_404(
        Incidencia,
        id=incidencia_id,
        tecnico_asignado__isnull=True,
        tipo_incidencia=especialidad.especialidad
    )

    incidencia.tecnico_asignado = especialidad
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
        especialidad = user.especialidad
    except Especialidad.DoesNotExist:
        return redirect('home')

    incidencia = get_object_or_404(
        Incidencia,
        id=incidencia_id,
        tecnico_asignado=especialidad
    )

    if incidencia.estado == 'cerrado':
        return redirect('detalle_incidencia', incidencia_id=incidencia.id)

    nuevo_estado = request.POST.get('estado')
    estados_validos = ['pendiente', 'en_espera', 'resuelto', 'cerrado']

    if nuevo_estado in estados_validos and nuevo_estado != incidencia.estado:
        HistorialEstadoIncidencia.objects.create(
            incidencia=incidencia,
            estado_anterior=incidencia.estado,
            estado_nuevo=nuevo_estado,
            cambiado_por=user
        )
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


@login_required
def detalle_incidencia(request, incidencia_id):
    user = request.user
    incidencia = get_object_or_404(Incidencia, id=incidencia_id)

    es_admin = (
        user.is_superuser or
        user.groups.filter(name='Administrador').exists()
    )
    es_usuario_creador = incidencia.usuario_creador == user
    es_tecnico = user.groups.filter(name='Técnicos').exists()
    es_tecnico_asignado = False
    puede_autoasignar = False

    if es_tecnico and hasattr(user, 'especialidad'):
        especialidad = user.especialidad
        es_tecnico_asignado = incidencia.tecnico_asignado == especialidad
        puede_autoasignar = (
            incidencia.tecnico_asignado is None and
            incidencia.tipo_incidencia == especialidad.especialidad
        )

    if not (es_admin or es_usuario_creador or es_tecnico_asignado or puede_autoasignar):
        return redirect('home')

    historial = incidencia.historial_estados.order_by('-fecha_cambio')

    context = {
        'incidencia': incidencia,
        'historial': historial,
        'es_tecnico': es_tecnico,
        'es_tecnico_asignado': es_tecnico_asignado,
        'puede_autoasignar': puede_autoasignar
    }

    return render(request, 'incidencias/detalle_incidencia.html', context)
