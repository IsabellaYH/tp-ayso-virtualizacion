"""Funciones de validación para la aplicación de gestión de tareas."""


def validar_tarea(texto):
    """Valida que el texto de una tarea no esté vacío."""
    return bool(texto and texto.strip())


def validar_opcion_menu(opcion, minimo=1, maximo=5):
    """Valida que la opción del menú sea un entero dentro del rango permitido."""
    try:
        valor = int(opcion)
    except ValueError:
        return None

    if minimo <= valor <= maximo:
        return valor
    return None
