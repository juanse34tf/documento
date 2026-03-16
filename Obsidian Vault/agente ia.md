Google AI ofrece una gama de modelos de chat avanzados que podemos usar en LangChain, permitiendo el uso de características como **invocación de herramientas**, **streaming de tokens**, y mucho más.

En esta clase, aprenderemos a utilizar los modelos de chat de **Google AI** con LangChain, específicamente los modelos **Gemini**.

Exploraremos cómo conectarnos a estos modelos, generar respuestas en diálogos, y cómo aprovechar las herramientas de Google para personalizar la seguridad y el rendimiento de nuestras aplicaciones de chat.

---

### **Google AI vs Google Cloud Vertex AI**

Google ofrece acceso a los modelos **Gemini** a través de dos plataformas diferentes:

1. **Google AI (Gemini):** Requiere solo una cuenta de Google y una clave API. Esta opción es ideal para proyectos rápidos o personales.
2. **Google Cloud Vertex AI:** Ofrece características empresariales como claves de encriptación personalizadas y redes privadas. Requiere una cuenta de Google Cloud y facturación activa.

Para esta clase, utilizaremos **Google AI**, que es más sencillo y rápido de configurar.

---

### **Configuración de Google AI en LangChain**

### **Paso 1: Crear una Cuenta en Google y Obtener una API Key**

Para utilizar los modelos de Google AI, necesitas obtener una **clave API** siguiendo estos pasos:

1. Visita [Google AI](https://ai.google.dev/gemini-api/docs/api-key) y genera una API key.
2. Guarda la clave para configurarla más adelante.

### **Paso 2: Configurar la Clave API**

Una vez que tengas tu API key, debes configurarla como una variable de entorno para que LangChain pueda acceder a ella:

```python
import getpass
import os

os.environ["GOOGLE_API_KEY"] = getpass.getpass("Introduce tu clave API de Google AI: ")
```

Esto asegurará que tu clave API se mantenga segura y accesible sin estar directamente expuesta en el código.

---

### **Instalación de la Integración de Google AI en LangChain**

Para interactuar con los modelos de Google AI, necesitamos instalar el paquete de integración **langchain-google-genai**. Utiliza el siguiente comando:

```bash
pip install -qU langchain-google-genai
```

---

# [REFERENCIA 1](https://ai.google.dev/gemini-api/docs/models/gemini?hl=es-419)

# [REFERENCIA 2](https://python.langchain.com/v0.2/docs/integrations/chat/google_generative_ai/)

### **Generar Respuestas con Google AI**

Con la integración instalada y la API key configurada, podemos instanciar un modelo de Google AI y generar una respuesta. Aquí usaremos el modelo **Gemini 1.5-pro**:

```python
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
```

```python
messages = [
    (
        "system",
        "You are a helpful assistant that translates English to French. Translate the user sentence.",
    ),
    ("human", "I love programming."),
]
ai_msg = llm.invoke(messages)
ai_msg

print(ai_msg.content)
```

---

### **Encadenar el Modelo con Plantillas de Prompts**

Podemos mejorar la funcionalidad del modelo encadenándolo con plantillas de prompts. Esto permite adaptar el comportamiento del modelo de forma dinámica, por ejemplo, para traducciones entre diferentes idiomas.

```python
from langchain_core.prompts import ChatPromptTemplate

# Crear una plantilla de prompt para traducciones
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Eres un asistente útil que traduce {input_language} a {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

# Encadenar la plantilla con el modelo de Google AI
chain = prompt | llm

# Invocar la cadena con parámetros específicos
chain.invoke(
    {
        "input_language": "English",
        "output_language": "German",
        "input": "I love programming.",
    }
)
```

La respuesta generada será:

```python
pythonCopiar código
"Ich liebe das Programmieren. \n"

```

---

### **Configuración de Seguridad en los Modelos Gemini**

Los modelos **Gemini** de Google AI tienen configuraciones de seguridad por defecto que ayudan a prevenir la generación de contenido dañino. Sin embargo, estas configuraciones pueden ser ajustadas para adaptarse mejor a las necesidades de tu aplicación.

Por ejemplo, si estás recibiendo muchos “Safety Warnings” en tus respuestas, puedes modificar los **umbrales de bloqueo** para categorías específicas de contenido:

```python
pythonCopiar código
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    HarmBlockThreshold,
    HarmCategory,
)

# Desactivar el bloqueo para contenido peligroso
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    safety_settings={
        HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
    },
)

```

Este código ajusta la configuración de seguridad para permitir contenido que normalmente podría estar bloqueado por defecto.

---

### **Conclusión**

Los modelos de Google ofrecen una solución robusta para construir aplicaciones de chat avanzadas, desde la configuración básica hasta la generación de respuestas y el uso de plantillas de prompts, hemos explorado cómo ajustar las configuraciones de seguridad para personalizar el comportamiento del modelo según las necesidades de tu aplicación.utilizando los modelos de **Google AI** con LangChain específicamente con Gemini.

**Ejercicio Final:**

- Configura tu clave API de Google AI y genera una conversación básica con el modelo.
- Modifica la configuración de seguridad del modelo para ajustar los umbrales de bloqueo y experimenta con diferentes respuestas.
- Reflexiona sobre cómo podrías integrar los modelos de Google AI en un proyecto para mejorar la interacción con los usuarios.

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(  
model=“gemini-1.5-pro”,  
temperature=0,  
max_tokens=None,  
timeout=None,  
max_retries=2,  
#other params…  
)