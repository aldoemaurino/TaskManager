import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def create_simple_tasks(description):
    
    if not client.api_key:
        return["ERROR: La Api Key de OPENAI no está configurada."]
    
    try:
        prompt = f"""Desglosa la siguiente tarea compleja en 3 a 5 subtareas simples y accionables.
        Tarea: {description}
        Formato de respuesta:
        - subtarea1
        - subtarea2
        - subtarea3
        - etc
        Responde solo con la lista de Subtareas, una por linea, empezndo cada linea con un guión"""
        params = {
            "model": "gpt-5",
            "messages":[
                {"role": "system", "content": "Eres un ascistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role": "user", "content": prompt}
            ],
            "max_completions_tokens": 300,
            "verbosity": "medium",
            "reasoning_effort": "minimal" 
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []

        for line in content.split("\n"):
            line = line.stip()
            if line and line.startswith("-"):
                subtasks =  line[1:].strip()
                if subtasks:
                    subtasks.append(subtasks)
        
        return subtasks if subtasks else ["ERROR: No se ha podido generar ninguna Subtarea"]
        
    except Exception:
        return["ERROR: No se ha podido realizar la conexión con OPENAI."]