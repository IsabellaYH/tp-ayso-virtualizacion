"""Punto de entrada de la aplicación de consola para gestionar tareas."""

from gestor_tareas import agregar_tarea, buscar_tareas, eliminar_tarea, listar_tareas
from validaciones import validar_opcion_menu


MENU = """
=== Sistema de Gestión de Tareas ===
1. Agregar tarea
2. Listar tareas
3. Buscar tareas
4. Eliminar tarea
5. Salir
Seleccione una opción: """


def main():
    """Ejecuta el menú interactivo principal."""
    tareas = []

    while True:
        try:
            opcion_ingresada = input(MENU)
        except EOFError:
            print("\nEntrada finalizada. Saliendo del sistema...")
            break

        opcion = validar_opcion_menu(opcion_ingresada)
        if opcion is None:
            print("Opción inválida. Ingrese un número entre 1 y 5.")
            continue

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            exito, mensaje = agregar_tarea(tareas, descripcion)
            print(mensaje)

        elif opcion == 2:
            print("\n--- Lista de tareas ---")
            for linea in listar_tareas(tareas):
                print(linea)

        elif opcion == 3:
            termino = input("Ingrese término a buscar: ")
            resultados, error = buscar_tareas(tareas, termino)
            if error:
                print(error)
            elif resultados:
                print("\nCoincidencias encontradas:")
                for indice, tarea in resultados:
                    print(f"{indice}. {tarea}")
            else:
                print("No se encontraron tareas con ese criterio.")

        elif opcion == 4:
            numero = input("Ingrese el número de la tarea a eliminar: ")
            exito, mensaje = eliminar_tarea(tareas, numero)
            print(mensaje)

        elif opcion == 5:
            print("Saliendo del sistema. ¡Hasta luego!")
            break


if __name__ == "__main__":
    main()
