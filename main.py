
from task_manager import TaskManager
from ai_service import create_simple_tasks

def print_menu():

        print("\n--- Gestor de Tares Inteligente ---")
        print("1. Añadir Tareas")
        print("2. Añadir Tarea Compleja (con IA)")
        print("3. Listar Tareas")
        print("4. Completar Tarea")
        print("5. Eliminar Tarea")
        print("6. Salir")

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
                    description = input("Descripción de la Tarea Compleja: ")
                    subtasks = create_simple_tasks(description)
                    for subtask in subtasks:
                        if not subtask.startswith("ERROR:"):
                            manager.add_task(subtask)
                        else:
                            print(subtask)
                            break
                case 3:
                    manager.list_tasks()
                case 4:
                    id = int(input("ID de la tarea a completar: "))
                    manager.complete_task(id)
                case 5:
                    id = int(input("ID de la tarea a borrar: "))
                    manager.delete_task(id)
                case 6:
                    print("Saliendo....")
                    break
                case _:
                    print("Opción no válida, seleccione otra")
        
        except ValueError:
            print("Opción no válida, seleccione otra")

if __name__=="__main__":
    main()