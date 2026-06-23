# tp-agyso-virtualizacion

## Descripción del proyecto
Aplicación de consola en Python 3 para gestionar tareas (agregar, listar, buscar y eliminar) con validaciones básicas de entrada.

## Objetivo académico
Demostrar la ejecución de una aplicación simple dentro de máquinas virtuales clonadas en VirtualBox, priorizando el análisis de virtualización, snapshots y aislamiento.

## Tecnologías utilizadas
- Python 3
- VirtualBox (snapshots y clones)
- Markdown para documentación

## Estructura del repositorio
```text
tp-virtualizacion-python/
├── src/
│   ├── main.py
│   ├── gestor_tareas.py
│   └── validaciones.py
├── docs/
│   ├── informe.md
│   └── evidencias.md
├── capturas/
├── README.md
├── requirements.txt
└── .gitignore
```

## Instrucciones de ejecución
1. Verificar Python 3 instalado.
2. Ir al directorio del proyecto.
3. Ejecutar:

```bash
python src/main.py
```

## Ejemplos de uso
- Agregar tarea: elegir opción `1` y escribir una descripción.
- Listar tareas: elegir opción `2`.
- Buscar tarea: elegir opción `3` y escribir un término.
- Eliminar tarea: elegir opción `4` e ingresar número de la tarea.
- Salir: elegir opción `5`.

## Evidencias de virtualización
Registrar capturas en `capturas/` y documentar resultados en `docs/evidencias.md`.

## Snapshots en VirtualBox
1. Crear una VM base con Python instalado.
2. Tomar un snapshot inicial.
3. Ejecutar pruebas del sistema.
4. Restaurar snapshot para volver al estado inicial.

## Clones en VirtualBox
- Crear `AlumnoA_VM` y `AlumnoB_VM` a partir de la VM base.
- Usar clones completos para aislar estado.
- Ejecutar la app en ambas VMs y comparar resultados.

## Validación de aislamiento entre AlumnoA_VM y AlumnoB_VM
1. En `AlumnoA_VM`, agregar tareas y registrar resultado.
2. En `AlumnoB_VM`, iniciar la app limpia y verificar que no aparezcan tareas de `AlumnoA_VM`.
3. Documentar evidencia visual en `capturas/`.

## Video explicativo 
 - link drive https://drive.google.com/file/d/1HyTnPtenFaaSbkzPmn4Z3taWRGlsdGAy/view?usp=sharing

 ## Capturas y evidencias 
  - TPI_AYSO_Virtualizacion.pdf https://drive.google.com/file/d/1AqjsMBH5Ke_DF2B3MlxZav17ziYVFH4F/view?usp=sharing 
  