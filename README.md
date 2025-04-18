## ¿Qué es Ollama?
> Ollama es como un intermediario entre los modelos de IA y mi aplicación, se encarga de la parte tediosa de interpretar y enviar las consultas a los diferentes modelos en el formato que cada uno de ellos lo necesite.

## ¿Qué es FastAPI?
> FastAPI es un framework para construir APIs rápidas y eficientes. Ahorra mucho tiempo de desarrollo y mantenimiento.

## ¿Qué es el modelo deepseek-r1?
> Deepseek-r1 es un modelo de IA de lenguaje de código abierto que se utiliza para responder preguntas y proporcionar información.

## Uso de peticiones con stream=True
>

## ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?

## ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?

## ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?

## ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?


### activate project

```shell
source env/bin/activate

cd mi_proyecto/app
uvicorn main:app --reload

or

uvicorn app.main:app --reload

```