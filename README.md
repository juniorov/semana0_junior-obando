# Semana 0 - Junior Obando

# Table of Contents
1. [Tecnologías](#tecnologias)
2. [Configuración](#configuracion)
3. [Conceptos](#conceptos)


## 1. Tecnologías <a name="tecnologias"></a>
* [Python](https://www.python.org/): Lenguaje de programación de alto nivel, versátil y multiplataforma.
* [Fastapi](https://fastapi.tiangolo.com/): Framework para construir APIs rápidas y eficientes.
* [Pydantic](https://pydantic-docs.helpmanual.io/): Biblioteca para validación de datos.
* [Ollama](https://ollama.com/): Plataforma para la integración de modelos de IA.


## 2. Configuración del proyecto <a name="configuracion"></a>
1. Crear el entorno virtual `python -m venv env`
2. Activar el entorno virtual `source env/bin/activate`
3. Instalar las dependencias `pip install -r requirements.txt`
4. Configurar las variables de entorno `cp .env.example .env`
5. Ejecutar la aplicación `uvicorn app.main:app --reload`


## 3. Conceptos <a name="conceptos"></a>
### ¿Qué es Ollama?
> Ollama es como un intermediario entre los modelos de IA y mi aplicación, se encarga de la parte tediosa de interpretar y enviar las consultas a los diferentes modelos en el formato que cada uno de ellos lo necesite.

### ¿Qué es FastAPI?
> FastAPI es un framework para construir APIs rápidas y eficientes. Ahorra mucho tiempo de desarrollo y mantenimiento.

### ¿Qué es el modelo deepseek-r1?
> Deepseek-r1 es un modelo de IA de lenguaje de código abierto que se utiliza para responder preguntas y proporcionar información.

### Uso de peticiones con stream=True
> Permite recibir la respuesta mientras se genera, esto permite una mejor experiencia de usuario.

### ¿Cómo garantizar la escalabilidad de una API que consume modelos de IA pesados?
> Se podrían implementar diferentes técnicas para poder garantizar la escalabilidad de una API que consume modelos de IA pesados, como por ejemplo: balanceo de carga, procesamiento asíncrono, almacenamiento en caché, múltiples instancias de ollama, etc.

### ¿Qué parámetros de Ollama (ej: num_ctx, temperature) afectan el rendimiento/calidad de respuestas?
> Además de esos dos parámetros existen otros más que son capaces de influenciar en la calidad/rendimiento.
>
> `num_ctx` este en específico esta relacionado al historial de la conversación, un valor alto permite al modelo recordar más contexto de la conversación, pero esto puede afectar el tiempo de procesamientp y el uso de memoria.
>
> `temperature` este parámetro controla la aletoriedad de las respuestas, un valor cercano al 1 hará que el modelo a dar respuestas más creativas pero podrían ser un poco incoherentes, un valor cercano al 0 puede hacer que las respuestas sean más repetitivas o poco creativas.
> Se debe trabajar un valor intermedio para encontrar el equilibrio.
>
> Existen otro parametros como `num_gpu` que afecta a la tarjeta gráfica, `num_thread` afecta el numero de nucleos.

### ¿Qué estrategias usar para balancear carga entre múltiples instancias de Ollama?
> Se puede implementar estrategias como Round Robin, Least Connections, IP Hash, Response Time.
> Por ejemplo Round Robin distribuye secuencialmente las peticiones, es decir, la primera peticion va a la primera instancia, la segunda peticion va a la segunda instancia, etc.
>
> Least Connections distribuye las peticiones en función del número de conexiones, es decir, la peticion va a la instancia con menos conexiones.
>
> IP Hash distribuye las peticiones en función del IP del cliente, es decir, la peticion va a la instancia con el mismo IP.
>
> Response Time distribuye las peticiones en función del tiempo de respuesta, es decir, la peticion va a la instancia con el menor tiempo de respuesta.

### ¿Qué patrones de diseño (ej: CQRS, Singleton) son útiles para integrar modelos de IA en backend?
> Patrones como CQRS pueden optimizar las operaciones de lectura y escritura relacionadas con la IA. Singleton puede gestionar instancias únicas (aunque menos crítico con Ollama). Adapter puede unificar interfaces de diferentes modelos/servicios. Proxy puede añadir funcionalidades. El procesamiento asíncrono es fundamental para la concurrencia. Circuit Breaker mejora la resiliencia. Pub/Sub facilita la comunicación basada en eventos.
