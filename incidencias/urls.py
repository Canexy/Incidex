from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('incidencias/<int:incidencia_id>/autoasignar/', views.autoasignar_incidencia, name='autoasignar_incidencia'),
    path('incidencias/<int:incidencia_id>/estado/', views.cambiar_estado_incidencia, name='cambiar_estado_incidencia'),
    path('incidencias/nueva/', views.crear_incidencia, name='crear_incidencia'),
    path('incidencias/<int:incidencia_id>/', views.detalle_incidencia, name='detalle_incidencia'),
]
