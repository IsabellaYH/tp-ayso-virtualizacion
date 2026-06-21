# Evidencias de virtualización

## Evidencias sugeridas
Agregar capturas en la carpeta `capturas/` con los siguientes escenarios:

1. Ejecución en `AlumnoA_VM`.
2. Ejecución en `AlumnoB_VM`.
3. Snapshot creado antes de pruebas.
4. Restauración de snapshot.
5. Diferencia de estado entre clones.

## Validación de aislamiento
- Crear una tarea en `AlumnoA_VM`.
- Verificar que **no** aparezca en `AlumnoB_VM` si no se comparte almacenamiento.
- Documentar el resultado con capturas y fecha.
