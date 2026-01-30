
# Últimos cambios:
- Se ha mejorado la creación de usuarios desde la consola de administración.
- Se ha solucionado aquellos estados inválidos en la creación o modificación de usuarios desde la consola de administración. Se añade además un nuevo inline sobre la modificación de usuarios en el grupo Técnicos.

# Técnico:
## Fallos:
 ̶-̶ ̶E̶l̶ ̶t̶é̶c̶n̶i̶c̶o̶ ̶n̶o̶ ̶p̶u̶e̶d̶e̶ ̶v̶e̶r̶ ̶d̶e̶t̶a̶l̶l̶e̶s̶ ̶d̶e̶ ̶"̶I̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶ ̶d̶i̶s̶p̶o̶n̶i̶b̶l̶e̶s̶"̶ ̶s̶i̶n̶ ̶a̶u̶t̶o̶-̶a̶s̶i̶g̶n̶a̶r̶s̶e̶ ̶e̶n̶ ̶e̶s̶a̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶.̶ ̶T̶r̶a̶s̶ ̶e̶l̶l̶o̶,̶ ̶p̶u̶e̶d̶e̶ ̶v̶e̶r̶ ̶t̶o̶d̶o̶s̶ ̶l̶o̶s̶ ̶d̶e̶t̶a̶l̶l̶e̶s̶.̶
Se afinó la asignación de permisos para los técnicos.
̶-̶ ̶R̶e̶d̶i̶s̶e̶ñ̶a̶r̶ ̶l̶a̶ ̶l̶ó̶g̶i̶c̶a̶ ̶d̶e̶ ̶t̶e̶n̶e̶r̶ ̶u̶n̶a̶ ̶t̶a̶b̶l̶a̶ ̶T̶é̶c̶n̶i̶c̶o̶ ̶a̶l̶ ̶q̶u̶e̶ ̶a̶ñ̶a̶d̶i̶r̶ ̶s̶i̶ ̶e̶s̶ ̶H̶a̶r̶d̶w̶a̶r̶e̶ ̶o̶ ̶S̶o̶f̶t̶w̶a̶r̶e̶.̶ ̶E̶s̶o̶ ̶r̶e̶q̶u̶i̶e̶r̶e̶ ̶d̶o̶s̶ ̶p̶a̶s̶o̶s̶;̶ ̶C̶r̶e̶a̶r̶ ̶a̶l̶ ̶t̶é̶c̶n̶i̶c̶o̶ ̶y̶ ̶a̶s̶i̶g̶n̶a̶r̶l̶e̶ ̶e̶n̶ ̶u̶n̶a̶ ̶t̶a̶b̶l̶a̶ ̶a̶i̶s̶l̶a̶d̶a̶ ̶e̶n̶ ̶q̶u̶é̶ ̶e̶s̶t̶á̶ ̶e̶s̶p̶e̶c̶i̶a̶l̶i̶z̶a̶d̶o̶.̶
Se creó una lógica más adecuada al flujo Técnicos/Especialidad.

# Usuario:

# Administrador:
 ̶-̶ ̶C̶r̶e̶a̶r̶ ̶g̶r̶u̶p̶o̶ ̶'̶A̶d̶m̶i̶n̶i̶s̶t̶r̶a̶d̶o̶r̶'̶ ̶d̶e̶n̶t̶r̶o̶ ̶d̶e̶ ̶D̶j̶a̶n̶g̶o̶ ̶y̶ ̶a̶s̶i̶g̶n̶a̶r̶ ̶l̶a̶ ̶v̶i̶s̶t̶a̶ ̶a̶ ̶e̶s̶e̶ ̶g̶r̶u̶p̶o̶,̶ ̶c̶o̶m̶o̶ ̶e̶s̶t̶á̶ ̶h̶e̶c̶h̶o̶ ̶c̶o̶n̶ ̶l̶o̶s̶ ̶d̶e̶m̶á̶s̶.̶
Se creó un grupo Administrador y se asignó las diferentes vistas del mismo.

# General:
## Mejoras:
 ̶-̶ ̶A̶ñ̶a̶d̶i̶r̶ ̶l̶ó̶g̶i̶c̶a̶ ̶d̶e̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶ ̶c̶e̶r̶r̶a̶d̶a̶s̶:̶ ̶C̶u̶a̶n̶d̶o̶ ̶u̶n̶a̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶ ̶s̶e̶ ̶c̶i̶e̶r̶r̶a̶,̶ ̶d̶e̶b̶e̶ ̶d̶e̶s̶a̶p̶a̶r̶e̶c̶e̶r̶ ̶d̶e̶l̶ ̶t̶a̶b̶l̶ó̶n̶ ̶"̶M̶i̶s̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶ ̶a̶s̶i̶g̶n̶a̶d̶a̶s̶"̶ ̶d̶e̶l̶ ̶t̶é̶c̶n̶i̶c̶o̶.̶ ̶D̶e̶b̶e̶ ̶e̶x̶i̶s̶t̶i̶r̶ ̶u̶n̶ ̶h̶i̶s̶t̶o̶r̶i̶a̶l̶ ̶d̶e̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶ ̶p̶a̶r̶a̶ ̶c̶a̶d̶a̶ ̶t̶é̶c̶n̶i̶c̶o̶ ̶c̶o̶n̶ ̶t̶o̶d̶a̶s̶ ̶e̶s̶a̶s̶ ̶i̶n̶c̶i̶d̶e̶n̶c̶i̶a̶s̶ ̶c̶e̶r̶r̶a̶d̶a̶s̶,̶ ̶q̶u̶e̶ ̶a̶d̶e̶m̶á̶s̶ ̶n̶o̶ ̶p̶o̶d̶r̶á̶n̶ ̶s̶e̶r̶ ̶m̶o̶d̶i̶f̶i̶c̶a̶d̶a̶s̶.̶
Se creó una separación sobre incidencias disponibles y cerradas por cada técnico.
- Crear visual de la página (mockup) e implementarla.
-  ̶C̶o̶n̶t̶e̶m̶p̶l̶a̶r̶ ̶c̶a̶m̶b̶i̶o̶s̶ ̶a̶ ̶l̶o̶s̶ ̶n̶o̶m̶b̶r̶e̶s̶ ̶d̶e̶ ̶l̶a̶s̶ ̶t̶a̶b̶l̶a̶s̶, para una mejor visualización de ellas, acorde a su propósito. Ejemplo: incidencias_incidencia, no acaba de decir exactamente qué es. Pasa con casi todas.

## Fallos:
- Se asumen limitaciones técnicas por parte de Django que cambian la filosofía final del producto.
- No se conocen fallos funcionales activos en este momento.