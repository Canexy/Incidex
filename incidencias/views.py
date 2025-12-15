# Obliga a que el usuario esté autenticado para acceder a las vistas.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from django.views.decorators.http import require_POST

from .models import Incidencia, Tecnico, HistorialEstadoIncidencia
from .forms import IncidenciaForm

# Dependiendo del tipo de usuario, muestra diferentes paneles de control.
@login_required
def home(request):
    user = request.user
    context = {}

    # Usuario normal.
    if user.groups.filter(name='Usuarios').exists():
        incidencias = Incidencia.objects.filter(usuario_creador=user)
        context['tipo_panel'] = 'usuario'
        context['incidencias'] = incidencias

    # Técnico.
    elif user.groups.filter(name='Técnicos').exists():
        try:
            tecnico = user.tecnico
        except Tecnico.DoesNotExist:
            tecnico = None

        if tecnico:
            incidencias_disponibles = Incidencia.objects.filter(tipo_incidencia=tecnico.especialidad, tecnico_asignado__isnull=True)
            incidencias_asignadas = Incidencia.objects.filter(tecnico_asignado=tecnico)
            context['tipo_panel'] = 'tecnico'
            context['incidencias_disponibles'] = incidencias_disponibles
            context['incidencias_asignadas'] = incidencias_asignadas
        else:
            context['tipo_panel'] = 'tecnico_sin_perfil'

    # Administrador (o rol especial de control).
    else:
        incidencias = Incidencia.objects.all()
        context['tipo_panel'] = 'admin'
        context['incidencias'] = incidencias

    return render(request, "incidencias/home.html", context)

# Acción para que un técnico se autoasigne una incidencia disponible.
@login_required
@require_POST
def autoasignar_incidencia(request, incidencia_id):
    user = request.user

    # Solo técnicos.
    if not user.groups.filter(name='Técnicos').exists():
        return redirect('home')

    try:
        tecnico = user.tecnico
    except:
        return redirect('home')

    incidencia = get_object_or_404(Incidencia, id=incidencia_id, tecnico_asignado__isnull=True, tipo_incidencia=tecnico.especialidad)
    incidencia.tecnico_asignado = tecnico
    incidencia.estado = 'abierto'
    incidencia.save()

    return redirect('home')

# Acción para que un técnico cambie el estado de una incidencia asignada.
@login_required
@require_POST
def cambiar_estado_incidencia(request, incidencia_id):
    user = request.user

    # Solo técnicos.
    if not user.groups.filter(name='Técnicos').exists():
        return redirect('home')

    try:
        tecnico = user.tecnico
    except Tecnico.DoesNotExist:
        return redirect('home')

    incidencia = get_object_or_404(Incidencia, id=incidencia_id, tecnico_asignado=tecnico)
    nuevo_estado = request.POST.get('estado')
    estados_validos = ['pendiente', 'en_espera', 'resuelto', 'cerrado']

    if nuevo_estado in estados_validos and nuevo_estado != incidencia.estado:
        HistorialEstadoIncidencia.objects.create(incidencia=incidencia, estado_anterior=incidencia.estado, estado_nuevo=nuevo_estado, cambiado_por=user)
        incidencia.estado = nuevo_estado
        incidencia.save()

    return redirect('home')

#Creación de una nueva incidencia por parte de un usuario.
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

# Vista detallada de una incidencia.
@login_required
def detalle_incidencia(request, incidencia_id):
    user = request.user
    incidencia = get_object_or_404(Incidencia, id=incidencia_id)

    es_admin = user.is_superuser
    es_usuario_creador = incidencia.usuario_creador == user
    es_tecnico = user.groups.filter(name='Técnicos').exists()
    es_tecnico_asignado = False
    puede_autoasignar = False

    if es_tecnico and hasattr(user, 'tecnico'):
        tecnico = user.tecnico
        es_tecnico_asignado = incidencia.tecnico_asignado == tecnico
        puede_autoasignar = (incidencia.tecnico_asignado is None and incidencia.tipo_incidencia == tecnico.especialidad)

    if not (es_admin or es_usuario_creador or es_tecnico_asignado):
        return redirect('home')

    historial = incidencia.historial_estados.order_by('-fecha_cambio')
    context = {'incidencia': incidencia, 'historial': historial, 'es_tecnico': es_tecnico, 'es_tecnico_asignado': es_tecnico_asignado, 'puede_autoasignar': puede_autoasignar}

    return render(request, 'incidencias/detalle_incidencia.html', context)
