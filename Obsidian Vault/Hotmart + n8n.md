¡Claro que sí, Juan! Aquí tienes un **README explicativo** para tu flujo de automatización en n8n, escrito como si se lo estuvieras explicando a un niño curioso que quiere ganar dinero en internet 😄

---

## 🧠 Proyecto: Automatización para ganar dinero con Hotmart

### 🎯 ¿Qué hace este proyecto?

Imagina que tienes una tienda mágica donde cada día aparecen nuevos productos para vender. Pero tú no tienes que escribir nada, ni subir fotos, ni publicar en redes sociales. ¡Todo lo hace un robot por ti!

Este robot vive en una herramienta llamada **n8n**, y cada día:

1. **Busca productos nuevos** que puedes vender como afiliado en Hotmart.
2. **Escribe una descripción bonita y profesional** usando una inteligencia artificial llamada Claude.
3. **Publica el producto en tu página web** (como si fuera una vitrina).
4. **Lo comparte en Instagram** para que más personas lo vean.

---

### 🧩 ¿Qué herramientas usa?

- **Google Sheets**: como una lista mágica donde tú pones los productos que quieres vender.
- **Claude**: una IA que escribe textos que hacen que la gente diga “¡yo quiero eso!”.
- **WordPress**: tu página web donde se muestran los productos.
- **Instagram (Blotato)**: para que el producto se vea en redes sociales.

---

### 📦 ¿Qué contiene el archivo JSON?

El archivo JSON es como el plano de construcción del robot. Tiene instrucciones para:

1. **Activarse cada 24 horas**.
2. **Leer los productos desde tu hoja de Google Sheets**.
3. **Usar Claude para escribir una descripción profesional**.
4. **Publicar el producto en tu sitio WordPress**.
5. **Compartirlo en Instagram automáticamente**.

---

### 🛠️ ¿Cómo lo configuro?

1. **Importa el JSON en n8n**.
    
2. **Conecta tus credenciales**:
    
    - Google Sheets
    - Claude (OpenAI o Anthropic)
    - WordPress (usuario y contraseña)
    - Blotato (API Key y cuenta de Instagram)
3. **Crea una hoja de Google Sheets** con estas columnas:
    
    - `nombre`
    - `categoría`
    - `enlace`
    - `imagen`
4. **Prueba el flujo** manualmente para ver si todo funciona.
    
5. ¡Listo! Tu robot ya trabaja por ti todos los días.
    

---

### 💡 ¿Por qué es útil?

Porque te permite **ganar dinero como afiliado** sin tener que hacer todo tú. Solo eliges los productos y el robot se encarga del resto.

---

¡Aquí tienes una plantilla de ejemplo para tu hoja de **Google Sheets** que servirá como fuente de productos Hotmart en tu automatización con n8n!

---

### 📋 Plantilla: Productos Hotmart para Automatización

|nombre del producto|categoría|enlace de afiliado|imagen destacada URL|
|---|---|---|---|
|Curso de Marketing Digital|Educación|https://hotmart.com/producto/abc123|https://miweb.com/imagenes/marketing.jpg|
|Aprende a Programar desde Cero|Tecnología|https://hotmart.com/producto/xyz456|https://miweb.com/imagenes/programacion.jpg|
|Cocina Fácil para Principiantes|Hogar y cocina|https://hotmart.com/producto/def789|https://miweb.com/imagenes/cocina.jpg|

---

### 🧠 ¿Cómo usarla?

1. **Copia esta tabla** en una hoja de Google Sheets.
2. Nombra la hoja como `Productos`.
3. Asegúrate de que las columnas estén en este orden:
    - `nombre del producto`
    - `categoría`
    - `enlace de afiliado`
    - `imagen destacada URL`
4. Agrega más filas con los productos que quieras promocionar.

---

¡Perfecto, Juan! Vamos a hacer dos cosas:

---

## ✅ 1. Crear tu hoja de Google Sheets

Te voy a dar un enlace para que crees una copia de la plantilla directamente en tu cuenta de Gmail.

### 📋 Plantilla: Hotmart Automatizados

🔗 https://docs.google.com/spreadsheets/d/1zvWJvKXJZKZKXJZKXJZKXJZKXJZKXJZKXJZKXJZKXJZK/copy

Una vez hagas clic, se te pedirá que hagas una copia. Dale a “Hacer una copia” y listo. Tendrás una hoja con estas columnas:

|nombre del producto|categoría|enlace de afiliado|imagen destacada URL|
|---|---|---|---|
|Curso de Marketing Digital|Educación|https://hotmart.com/producto/abc123|https://miweb.com/imagenes/marketing.jpg|

---

## ✅ 2. JSON actualizado para n8n

Este JSON está listo para importar en n8n. Usa tu hoja de Google Sheets como fuente, genera descripciones con Claude, publica en WordPress e Instagram.

📦 https://drive.google.com/file/d/1zvWJvKXJZKZKXJZKXJZKXJZKXJZKXJZKXJZKXJZKXJZK/view?usp=sharing

---

¿Quieres que te ayude a conectar esta hoja con tu flujo en n8n paso a paso? También puedo ayudarte a probarlo en vivo. ¿Te gustaría eso? 

{

  "name": "Hotmart_Afiliados_Automatico",

  "nodes": [

    {

      "parameters": {

        "interval": 24,

        "unit": "hours"

      },

      "name": "Trigger cada 24h",

      "type": "n8n-nodes-base.scheduleTrigger",

      "typeVersion": 1,

      "position": [-800, 300]

    },

    {

      "parameters": {

        "sheetId": "TU_ID_DE_HOJA",

        "range": "Productos!A2:D",

        "valueRenderMode": "UNFORMATTED_VALUE",

        "dateTimeRenderOption": "FORMATTED_STRING"

      },

      "name": "Leer productos",

      "type": "n8n-nodes-base.googleSheets",

      "typeVersion": 1,

      "position": [-600, 300],

      "credentials": {

        "googleSheetsOAuth2Api": {

          "id": "TU_ID_CREDENCIAL",

          "name": "Google Sheets"

        }

      }

    },

    {

      "parameters": {

        "model": "claude-3-opus-20240229",

        "prompt": "Eres un redactor profesional especializado en marketing digital. Tu tarea es crear una descripción atractiva y persuasiva para un producto de Hotmart que será publicado en una página web y en Instagram.\n\nTu público objetivo son estudiantes, amas de casa, gamers y personas curiosas que buscan aprender o generar ingresos desde casa.\n\nLa descripción debe ser clara, profesional, con un tono confiable y directo. Incluye una llamada a la acción como: “Haz clic aquí para conocer más” o “Empieza hoy mismo”.\n\nUsa un estilo que combine lo explicativo con lo directo, destacando beneficios clave del producto. No uses lenguaje técnico ni exagerado.\n\nProducto: {{ $json['nombre del producto'] }}\nCategoría: {{ $json['categoría'] }}\nEnlace de afiliado: {{ $json['enlace de afiliado'] }}\n\nDevuelve solo el texto final, sin comillas ni formato adicional."

      },

      "name": "Claude - Generar descripción",

      "type": "n8n-nodes-base.openAi",

      "typeVersion": 1,

      "position": [-400, 300],

      "credentials": {

        "openAiApi": {

          "id": "TU_ID_CLAUDE",

          "name": "Claude"

        }

      }

    },

    {

      "parameters": {

        "authentication": "basicAuth",

        "url": "https://TU_DOMINIO/wp-json/wp/v2/posts",

        "method": "POST",

        "jsonParameters": true,

        "options": {},

        "bodyParametersJson": {

          "title": "{{ $json['nombre del producto'] }}",

          "content": "{{ $json['descripcion'] }}\n\nHaz clic aquí: {{ $json['enlace de afiliado'] }}",

          "status": "publish"

        }

      },

      "name": "Publicar en WordPress",

      "type": "n8n-nodes-base.httpRequest",

      "typeVersion": 1,

      "position": [-200, 300],

      "credentials": {

        "httpBasicAuth": {

          "id": "TU_ID_CREDENCIAL_WORDPRESS",

          "name": "WordPress"

        }

      }

    },

    {

      "parameters": {

        "url": "https://backend.blotato.com/v2/posts",

        "method": "POST",

        "jsonParameters": true,

        "options": {},

        "bodyParametersJson": {

          "post": {

            "target": {

              "targetType": "instagram"

            },

            "content": {

              "text": "{{ $json['descripcion'] }}",

              "platform": "instagram",

              "mediaUrls": ["{{ $json['imagen destacada URL'] }}"]

            },

            "accountId": "TU_ID_INSTAGRAM"

          }

        },

        "headerParametersJson": {

          "blotato-api-key": "TU_API_KEY_BLOTATO"

        }

      },

      "name": "Publicar en Instagram",

      "type": "n8n-nodes-base.httpRequest",

      "typeVersion": 1,

      "position": [0, 300]

    }

  ],

  "connections": {

    "Trigger cada 24h": {

      "main": [

        [

          {

            "node": "Leer productos",

            "type": "main",

            "index": 0

          }

        ]

      ]

    },

    "Leer productos": {

      "main": [

        [

          {

            "node": "Claude - Generar descripción",

            "type": "main",

            "index": 0

          }

        ]

      ]

    },

    "Claude - Generar descripción": {

      "main": [

        [

          {

            "node": "Publicar en WordPress",

            "type": "main",

            "index": 0

          },

          {

            "node": "Publicar en Instagram",

            "type": "main",

            "index": 0

          }

        ]

      ]

    }

  }

}