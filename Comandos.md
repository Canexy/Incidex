# Comandos usados bajo MySQL

## Conexión a MySQL

```bash
$ ssh mario@10.1.2.200
$ password: 1996
$ sudo mysql
$ USE incidex;
$ SHOW TABLES;
$ DESCRIBE <tabla>;
```

## Ver todos los usuarios y grupos

```sql
SELECT u.id AS user_id, u.username, g.name AS group_name
FROM auth_user u
LEFT JOIN auth_user_groups ug ON u.id = ug.user_id
LEFT JOIN auth_group g ON ug.group_id = g.id;
```

## Ver todos los técnicos y su especialidad

```sql
SELECT t.id AS tecnico_id, u.username, t.especialidad
FROM incidencias_tecnico t
JOIN auth_user u ON t.usuario_id = u.id;
```

## Ver todas las incidencias

```sql
SELECT i.id, i.titulo, i.descripcion, i.criticidad, i.tipo_incidencia,
       i.estado, i.tecnico_asignado_id, u.username AS tecnico_nombre
FROM incidencias_incidencia i
LEFT JOIN auth_user u ON i.tecnico_asignado_id = u.id;
```

## Ver historial de estados de incidencias

```sql
SELECT h.id,
       h.incidencia_id,
       i.titulo,
       h.estado_anterior,
       h.estado_nuevo,
       h.fecha_cambio,
       u.username AS cambiado_por
FROM incidencias_historialestadoincidencia h
JOIN incidencias_incidencia i ON h.incidencia_id = i.id
LEFT JOIN auth_user u ON h.cambiado_por_id = u.id
ORDER BY h.fecha_cambio;
```

## Consultar incidencias por tipo de técnico

```sql
SELECT i.id, i.titulo, i.tipo_incidencia, u.username AS tecnico
FROM incidencias_incidencia i
JOIN auth_user u ON i.tecnico_asignado_id = u.id
WHERE i.tipo_incidencia = 'software';
```

# Más comandos

## Borrar incidencia/s

```sql
DELETE FROM incidencias_incidencia WHERE id = 1;
DELETE FROM incidencias_incidencia;
```

## Reiniciar AUTO_INCREMENT

```sql
ALTER TABLE incidencias_incidencia AUTO_INCREMENT = 1;
```