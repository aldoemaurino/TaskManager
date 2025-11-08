import json
import os
import sys
import pytest

# Asegurar que el directorio raíz del proyecto está en sys.path para poder importar task_manager
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from task_manager import TaskManager, Task


def test_anadir_y_listar_tareas(tmp_path, capsys):
	"""Probar add_task y list_tasks"""
	TaskManager.FILENAME = str(tmp_path / "tasks.json")
	mgr = TaskManager()
	mgr.add_task("Escribir tests")
	mgr.add_task("Arreglar bug")
	# limpiar la salida de add_task
	capsys.readouterr()
	mgr.list_tasks()
	captured = capsys.readouterr()
	out = captured.out
	assert "#1: Escribir tests" in out
	assert "#2: Arreglar bug" in out


def test_marcar_completada_y_persistencia(tmp_path, capsys):
	"""Probar complete_task y que se guarde en disco"""
	TaskManager.FILENAME = str(tmp_path / "tasks.json")
	mgr = TaskManager()
	mgr.add_task("Tarea A")
	capsys.readouterr()
	mgr.complete_task(1)
	captured = capsys.readouterr()
	assert "Tarea completada" in captured.out
	# Recargar manager para verificar persistencia
	mgr2 = TaskManager()
	assert len(mgr2._tasks) == 1
	assert mgr2._tasks[0].id == 1
	assert mgr2._tasks[0].description == "Tarea A"
	assert mgr2._tasks[0].completed is True


def test_eliminar_tarea_y_persistencia(tmp_path, capsys):
	"""Probar delete_task y persistencia"""
	TaskManager.FILENAME = str(tmp_path / "tasks.json")
	mgr = TaskManager()
	mgr.add_task("Quedarse")
	mgr.add_task("Eliminar")
	capsys.readouterr()
	mgr.delete_task(2)
	captured = capsys.readouterr()
	assert "Tarea eliminada: #2" in captured.out
	mgr2 = TaskManager()
	assert len(mgr2._tasks) == 1
	remaining = mgr2._tasks[0]
	assert remaining.id == 1
	assert remaining.description == "Quedarse"


def test_carga_archivo_no_existente(tmp_path):
	"""Si el fichero no existe, no debe fallar"""
	nonexist = tmp_path / "no_file.json"
	if nonexist.exists():
		nonexist.unlink()
	TaskManager.FILENAME = str(nonexist)
	mgr = TaskManager()
	assert mgr._tasks == []
	assert mgr._next_id == 1


def test_representacion_str_de_task():
	t1 = Task(5, "ejemplo", completed=False)
	t2 = Task(6, "ejemplo hecho", completed=True)
	s1 = str(t1)
	s2 = str(t2)
	assert "#5: ejemplo" in s1
	assert "#6: ejemplo hecho" in s2
	assert "✓" in s2


def test_persistencia_ids_despues_de_borrado(tmp_path):
	"""Comprobar que _next_id se calcula correctamente tras borrados"""
	TaskManager.FILENAME = str(tmp_path / "tasks.json")
	mgr = TaskManager()
	mgr.add_task("uno")
	mgr.add_task("dos")
	mgr.delete_task(2)
	mgr2 = TaskManager()
	assert mgr2._next_id == 2


def test_save_tasks_escribe_json_valido(tmp_path):
	TaskManager.FILENAME = str(tmp_path / "tasks.json")
	mgr = TaskManager()
	mgr.add_task("tarea json")
	with open(TaskManager.FILENAME, "r") as f:
		data = json.load(f)
	assert isinstance(data, list)
	assert data[0]["id"] == 1
	assert data[0]["description"] == "tarea json"
	assert data[0]["completed"] is False

