"""Lógica principal de gestión de tareas."""

from validaciones import validar_tarea


def agregar_tarea(tareas, descripcion):
    """Agrega una tarea válida a la lista."""
    if not validar_tarea(descripcion):
        return False, "Error: la tarea no puede estar vacía."

    tareas.append(descripcion.strip())
    return True, "Tarea agregada correctamente."


def listar_tareas(tareas):
    """Retorna una lista de texto con las tareas enumeradas."""
    if not tareas:
        return ["No hay tareas registradas."]
    return [f"{indice}. {tarea}" for indice, tarea in enumerate(tareas, start=1)]


def buscar_tareas(tareas, termino):
    """Busca tareas que contengan el término indicado."""
    if not validar_tarea(termino):
        return []

    termino_normalizado = termino.strip().lower()
    coincidencias = [
        (indice, tarea)
        for indice, tarea in enumerate(tareas, start=1)
        if termino_normalizado in tarea.lower()
    ]
    return coincidencias


def eliminar_tarea(tareas, numero_tarea):
    """Elimina una tarea por su número visible en pantalla."""
    try:
        indice = int(numero_tarea) - 1
    except ValueError:
        return False, "Error: ingrese un número válido."

    if indice < 0 or indice >= len(tareas):
        return False, "Error: el número de tarea no existe."

    tarea_eliminada = tareas.pop(indice)
    return True, f"Tarea eliminada: {tarea_eliminada}"
