# Importar las librerías necesarias
from fastapi import FastAPI
from pydantic import BaseModel, ValidationError, Field
import os
from dotenv import load_dotenv
import ollama

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Crear una instancia de FastAPI
app = FastAPI()

# Modelo de datos para recibir la pregunta
class Pregunta(BaseModel):
    texto: str = Field(
        ...,
        description="La pregunta a responder",
        min_length=5,
        max_length=500,
    )

# Endpoint para recibir preguntas y devolver respuestas
@app.post("/preguntar")
async def preguntar(pregunta: Pregunta):
    try:
        response = ollama.chat(
            model=os.getenv("MODELO"),
            messages=[
                {
                    "role": "user",
                    "content": pregunta.texto
                }
            ],
            stream=True
        )
        return {"data": response['message']['content']}
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=f"Error de validación: {e}")
    except ollama.APIError as e:
        raise HTTPException(status_code=300, detail=f"Error al comunicarse con Ollama: {e}")
    except Exception as e:
        raise HTTPException(status_code=300, detail=f"Ocurrió un error inesperado: {e}")