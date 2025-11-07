
from task_manager import TaskManager

def print_menu():

        print("\n--- Gestor de Tares Inteligente ---")
        print("1. Añadir Tares")
        print("2. Listar Tareas")
        print("3. Completar Tarea")
        print("4. Eliminar Tarea")
        print("5. Salir")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:
        
            choice = int(input("Elije una Opción: "))

            match choice:
                case 1:
                    description = input("Descripción de la Tarea: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                case 3:
                    id = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id)
                case 4:
                    id = int(input("ID de la tarea a borrar: "))
                    manager.delete_task(id)
                case 5:
                    print("Saliendo....")
                    break
                case _:
                    print("Opción no válida, seleccione otra")
        
        except ValueError:
            print("Opción no válida, seleccione otra")

if __name__=="__main__":
    main()