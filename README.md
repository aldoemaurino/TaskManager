# TaskManager

Proyecto minimalista de línea de comandos para gestionar tareas (añadir, listar, completar y borrar). Este repositorio contiene una implementación sencilla en Python y una batería de tests con pytest.

## Contenido

- `task_manager.py` - Implementación principal con las clases `Task` y `TaskManager`.
- `main.py` - (opcional) Punto de entrada para usar la aplicación desde la línea de comandos.
- `ai_service.py` - (auxiliar) ficheros adicionales del proyecto.
- `task.json` - Archivo por defecto donde se guardan las tareas (puede crearse por la aplicación).
- `tests/test_task_manager.py` - Tests unitarios escritos con `pytest` (están en castellano).
- `requirements.txt` - Dependencias del proyecto.

## Requisitos

- Python 3.8+ (recomendado 3.10 o superior)
- pip

Instala dependencias (opcional, sólo es necesario pytest para ejecutar tests):

```bash
pip install -r requirements.txt
# o, si sólo quieres pytest:
pip install pytest
```

> Nota: `requirements.txt` incluye paquetes usados en el proyecto más amplio; para ejecutar únicamente los tests normalmente basta `pytest`.

## Uso básico

La clase `TaskManager` guarda tareas en el fichero definido por `TaskManager.FILENAME` (por defecto `task.json`).

Ejemplos rápidos (desde Python):

```python
from task_manager import TaskManager

TaskManager.FILENAME = "task.json"  # opcional: cambiar fichero de guardado
mgr = TaskManager()
mgr.add_task("Comprar leche")
mgr.list_tasks()
mgr.complete_task(1)
mgr.delete_task(1)
```

Los métodos imprimen mensajes informativos (en castellano) y guardan automáticamente el estado en JSON.

## Tests

Los tests están en `tests/test_task_manager.py` y usan `pytest`.

Para ejecutar los tests:

```bash
pytest -q
```

Los tests usan `tmp_path` para aislar ficheros y `capsys` para capturar la salida impresa.

## Estructura de datos y contrato mínimo

- Task:
  - id (int)
  - description (str)
  - completed (bool)

- TaskManager (métodos principales):
  - add_task(description) -> añade y guarda
  - list_tasks() -> imprime tareas
  - complete_task(id) -> marca completada y guarda
  - delete_task(id) -> elimina y guarda
  - load_tasks() / save_tasks() -> manejo interno del JSON

Error modes y consideraciones:
- Si el fichero de tareas no existe, `TaskManager` inicia con una lista vacía.
- Si se intenta completar o borrar una tarea inexistente, se imprime un mensaje de error y no se lanza excepción.

## Ideas y siguientes pasos

- Añadir un CLI más completo (con argparse o click) en `main.py`.
- Añadir validaciones y manejo de IDs duplicados si se introducen por fuera.
- Añadir pruebas adicionales para casos límite (IDs inválidos, fichero corrupto JSON).

---

Si quieres, puedo:
- Ejecutar los tests aquí y mostrar los resultados.
- Añadir un `Makefile` o tareas en `pyproject.toml` para facilitar ejecutar tests.
- Mejorar el CLI y documentarlo en el README.
# TaskManager