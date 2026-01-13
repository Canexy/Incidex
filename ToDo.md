
# Últimos cambios:
- Migración a MySQL usando 10.1.2.200 al Proxmox del centro. Si este servidor no está encendido, no funcionará.

# Técnico:
## Fallos:
- El técnico no puede ver detalles de "Incidencias disponibles" sin auto-asignarse en esa incidencia. Tras ello, puede ver todos los detalles.

# Usuario:

# Administrador:

# General:
## Mejoras:
- Crear visual de la página (mockup) e implementarla.
- Añadir lógica de incidencias cerradas: Cuando una incidencia se cierra, debe desaparecer del tablón "Mis incidencias asignadas" del técnico. Debe existir un historial de incidencias para cada técnico con todas esas incidencias cerradas, que además no podrán ser modificadas.

## Fallos:
- Tras la integración de MySQL, los usuarios no pueden ver su panel. Es decir, un usuario básico no puede crear incidencias, o un técnico no puede ver las disponibles.