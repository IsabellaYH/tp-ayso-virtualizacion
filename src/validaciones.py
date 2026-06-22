"""Funciones de validación para la aplicación de gestión de tareas."""

LONGITUD_MAXIMA_TAREA = 200


def validar_tarea(texto):
    """Valida que el texto de una tarea no esté vacío ni supere la longitud máxima.

    Retorna True si el texto es válido, False en caso contrario.
    """
    if not isinstance(texto, str):
        return False
    texto_limpio = texto.strip()
    return bool(texto_limpio) and len(texto_limpio) <= LONGITUD_MAXIMA_TAREA


def validar_opcion_menu(opcion, minimo=1, maximo=5):
    """Valida que la opción del menú sea un entero dentro del rango permitido.

    Retorna el entero si es válido, o None si la opción es inválida.
    """
    if not isinstance(opcion, str):
        return None
    try:
        valor = int(opcion.strip())
    except ValueError:
        return None

    if minimo <= valor <= maximo:
        return valor
    return None