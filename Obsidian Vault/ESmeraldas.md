# Guía simplificada: Automatización con n8n para vender manillas de plata con esmeraldas

## Configuración inicial

1. **Crear cuenta en n8n**
    
    - Visita [n8n.cloud](https://n8n.cloud/) y regístrate
    - O instala localmente siguiendo las instrucciones en [docs.n8n.io](https://docs.n8n.io/)
2. **Primer acceso**
    
    - Inicia sesión en tu cuenta
    - Familiarízate con la interfaz: menú lateral izquierdo para navegar y área central para crear flujos

## Flujo 1: Captura de clientes potenciales

1. **Crear nuevo flujo**
    
    - Haz clic en "Workflows" y luego en "Create Workflow"
    - Nombra el flujo como "Captura de Clientes"
2. **Añadir nodo para entrada de datos**
    
    - Busca "Webhook" en la barra de búsqueda y selecciónalo
    - Mantén la configuración predeterminada y haz clic en "Execute Node"
    - Guarda la URL generada para colocarla en tu formulario web
3. **Añadir nodo para almacenar datos**
    
    - Haz clic en "+" y busca "Google Sheets" (o tu CRM preferido)
    - Conecta tus credenciales de Google
    - Selecciona la hoja donde guardarás los datos de clientes
    - Mapea los campos del formulario con las columnas de tu hoja
4. **Añadir nodo para enviar correo automático**
    
    - Haz clic en "+" y busca "Email" o "Gmail"
    - Conecta tu cuenta de correo
    - En "To" coloca el campo de email del cliente
    - Escribe un asunto atractivo
    - Redacta un mensaje de bienvenida con imágenes de tus manillas
5. **Activar el flujo**
    
    - Haz clic en "Active" en la parte superior
    - Ahora cada vez que alguien complete tu formulario se guardará en tu hoja y recibirá un correo

## Flujo 2: Publicaciones automáticas en redes sociales

1. **Crear nuevo flujo**
    
    - Nombra el flujo como "Publicaciones Automáticas"
2. **Programar frecuencia**
    
    - Busca y añade el nodo "Schedule"
    - Configura para que se ejecute en los días y horarios que quieras publicar
3. **Obtener contenido a publicar**
    
    - Añade nodo "Google Sheets"
    - Conecta con una hoja donde tengas preparado tu contenido
    - En esta hoja debes tener columnas para: texto, imagen, hashtags, etc.
4. **Publicar en redes sociales**
    
    - Añade nodos para cada red social (Instagram, Facebook)
    - Conecta tus cuentas de redes sociales
    - Mapea los campos de tu hoja a los campos de publicación
5. **Activar el flujo**
    
    - Las publicaciones se realizarán automáticamente según tu programación

## Flujo 3: Seguimiento a clientes después de comprar

1. **Crear nuevo flujo**
    
    - Nombra el flujo como "Seguimiento Post-Venta"
2. **Configurar entrada de datos de ventas**
    
    - Si tienes tienda online, usa el nodo específico (Shopify, WooCommerce)
    - Si vendes por otros medios, usa "Webhook" para introducir datos manualmente
3. **Programar primer correo de seguimiento**
    
    - Añade nodo "Wait" y configura para 3 días
    - Añade nodo "Email" para preguntar sobre satisfacción
4. **Programar segundo correo**
    
    - Añade otro nodo "Wait" para 30 días
    - Añade nodo "Email" con consejos de mantenimiento de las manillas
    - Incluye ofertas de nuevos modelos
5. **Activar el flujo**
    
    - El sistema enviará automáticamente los correos en los momentos programados

## Flujo 4: Ofertas para recuperar clientes inactivos

1. **Crear nuevo flujo**
    
    - Nombra el flujo como "Recuperación de Clientes"
2. **Programar revisión periódica**
    
    - Añade nodo "Schedule" para ejecutarse una vez por semana
3. **Identificar clientes inactivos**
    
    - Añade nodo "Google Sheets" o tu CRM
    - Configura para filtrar clientes sin compras en los últimos 60 días
4. **Generar ofertas personalizadas**
    
    - Añade nodo "Email"
    - Configura correo con descuento especial
    - Personaliza el mensaje mencionando productos vistos anteriormente
5. **Activar el flujo**
    
    - Cada semana el sistema identificará y enviará ofertas a clientes inactivos

## Consejos prácticos para implementación

1. **Empieza con un solo flujo**
    
    - Implementa primero el de captura de clientes
    - Cuando funcione bien, añade el siguiente
2. **Usa nombres claros**
    
    - Nombra cada nodo según su función para facilitar futuras ediciones
3. **Haz pruebas pequeñas**
    
    - Antes de activar, usa el botón "Execute" en cada nodo para verificar que funciona
4. **Documenta tus flujos**
    
    - Añade notas explicativas en cada nodo importante
5. **Revisa periódicamente**
    
    - Cada semana verifica que tus flujos funcionan correctamente
    - Ajusta según los resultados que obtengas

Siguiendo estos pasos podrás automatizar gran parte del marketing y ventas de tus manillas de plata con esmeraldas, permitiéndote llegar a más clientes con menos esfuerzo manual.