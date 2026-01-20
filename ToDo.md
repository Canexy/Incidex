
# Últimos cambios:
- Migración a MySQL usando 10.1.2.200 al Proxmox del centro. Si este servidor no está encendido, no funcionará.

# Técnico:
## Fallos:
- El técnico no puede ver detalles de "Incidencias disponibles" sin auto-asignarse en esa incidencia. Tras ello, puede ver todos los detalles.

# Usuario:

# Administrador:
- Crear grupo 'Administrador' dentro de Django y asignar la vista a ese grupo, como está hecho con los demás.

# General:
## Mejoras:
- Crear visual de la página (mockup) e implementarla.
- Añadir lógica de incidencias cerradas: Cuando una incidencia se cierra, debe desaparecer del tablón "Mis incidencias asignadas" del técnico. Debe existir un historial de incidencias para cada técnico con todas esas incidencias cerradas, que además no podrán ser modificadas.

## Fallos:
✓  ̶T̶r̶a̶s̶ ̶l̶a̶ ̶i̶n̶t̶e̶g̶r̶a̶c̶i̶ó̶n̶ ̶d̶e̶ ̶M̶y̶S̶Q̶L̶,̶ ̶l̶o̶s̶ ̶u̶s̶u̶a̶r̶i̶o̶s̶ ̶n̶o̶ ̶p̶u̶e̶d̶e̶n̶ ̶v̶e̶r̶ ̶s̶u̶ ̶p̶a̶n̶e̶l̶.̶ ̶E̶s̶ ̶d̶e̶c̶i̶r̶,̶ ̶u̶n̶ ̶u̶s̶u̶a̶r̶i̶o̶ ̶b̶á̶s̶i̶c̶o̶ ̶n̶o̶ ̶p̶u̶e̶d̶e̶ ̶c̶r̶e̶a̶r̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶,̶ ̶o̶ ̶u̶n̶ ̶t̶é̶c̶n̶i̶c̶o̶ ̶n̶o̶ ̶p̶u̶e̶d̶e̶ ̶v̶e̶r̶ ̶l̶a̶s̶ ̶d̶i̶s̶p̶o̶n̶i̶b̶l̶e̶s̶.̶
La solución pasó por recrear de nuevo la base de datos y crear los grupos 'Técnicos' y 'Usuarios' dentro de Django (/admin). Hecho eso, se asignó manualmente a cada usuario.