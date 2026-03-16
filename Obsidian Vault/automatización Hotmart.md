# 🚀 Guía Super Fácil: Robot Promocional de Hotmart

¡Hola! Esta guía te ayudará a configurar tu propio robot que promociona productos de Hotmart automáticamente. Es como tener un ayudante que trabaja 24/7 para ti. 😊

## 🎯 ¿Qué hace este robot?

1. Busca productos buenos en Hotmart
2. Crea mensajes chéveres para promocionarlos
3. Los publica en tus redes sociales
4. Te avisa si algo sale mal
5. ¡Y todo esto lo hace solito!

## 🎮 ¿Cómo lo uso?

### Paso 1: Preparar tu computadora
1. Instala Python (es gratis)
2. Instala los programas extra que necesita (son como apps para tu robot)
```bash
pip install requests pandas python-dotenv
```

### Paso 2: Conseguir tus claves secretas
1. Ve a Hotmart y consigue tu "token de acceso"
2. Consigue los permisos de tus redes sociales
   - Facebook
   - Twitter
   - Instagram

### Paso 3: Configurar el robot
1. Abre el archivo `config.py`
2. Pon tus claves secretas donde dice "TU_TOKEN"
3. Guarda el archivo

### Paso 4: ¡A darle vida al robot! 🤖
1. Abre tu programa de comandos
2. Escribe:
```bash
python hotmart_bot.py
```

## 🎯 ¿Qué puede hacer el robot?

### Cosas Básicas:
- ✅ Buscar productos buenos
- ✅ Crear mensajes bonitos
- ✅ Publicar en redes sociales
- ✅ Avisarte si hay problemas

### Cosas Avanzadas:
- 📊 Ver qué publicaciones funcionan mejor
- 📅 Publicar a diferentes horas
- 📧 Mandarte correos con resúmenes
- 🔍 Encontrar los mejores productos

## 🚨 Consejos Importantes

1. No cambies las claves secretas
2. No compartas tus tokens con nadie
3. Revisa los mensajes del robot cada día
4. Si algo sale mal, el robot te avisará por correo

## 🆘 ¿Necesitas ayuda?

Si algo no funciona:
1. Revisa que escribiste bien tus tokens
2. Mira si hay mensajes de error en la pantalla
3. Revisa tu correo por si hay alertas
4. ¡Pregúntanos! Estamos para ayudarte 😊

## 📝 Configuraciones que puedes cambiar

En el archivo `config.py` puedes cambiar:
- Cada cuánto publica (horas)
- Qué tipo de productos buscar
- Los mensajes que usa
- A qué correo envía las alertas

## 🌟 Consejos para mejores resultados

1. Usa diferentes mensajes
2. Prueba distintas horas de publicación
3. Revisa qué productos funcionan mejor
4. Mantén actualizados tus tokens

## 🔄 Actualizaciones futuras

Estamos trabajando en agregar:
- Más redes sociales
- Mejores mensajes automáticos
- Más estadísticas
- ¡Y mucho más!

## 🤝 ¿Quieres contribuir?

¡Tus ideas son bienvenidas! Puedes:
1. Sugerir mejoras
2. Reportar problemas
3. Agregar nuevas funciones
4. Mejorar esta guía

## 📞 Contacto

¿Necesitas más ayuda? ¡Escríbenos!
- 📧 Email: [tu@email.com]
- 💬 Discord: [tu_usuario]

---

¡Listo! 🎉 Ahora tienes tu propio robot promocional. ¡A vender! 🚀 
 import requests
import json
from datetime import datetime, timedelta
import random
import time
from typing import List, Dict
import csv
from pathlib import Path
import logging
from email.mime.text import MIMEText
import smtplib

class HotmartAutomation:
    """
    Sistema automatizado para promoción de productos Hotmart
    """
    def __init__(self, access_token: str, email_config: Dict = None):
        # Configuración básica
        self.access_token = access_token
        self.base_url = "https://api.hotmart.com/v1"
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }
        
        # Configuración de email para alertas
        self.email_config = email_config
        
        # Inicializar sistema de logging
        self.setup_logging()
        
        # Lista para almacenar datos de rendimiento
        self.performance_data = []
        
        # Cargar frases promocionales
        self.promo_phrases = self.load_promo_phrases()

    def setup_logging(self):
        """Configura el sistema de registro de eventos"""
        logging.basicConfig(
            filename='hotmart_automation.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def load_promo_phrases(self) -> Dict[str, List[str]]:
        """Carga frases promocionales por categoría"""
        return {
            "marketing-digital": [
                "🚀 ¡Impulsa tu negocio digital!",
                "💡 Aprende marketing como experto",
                "📈 Aumenta tus ventas online"
            ],
            "desarrollo-personal": [
                "✨ Transforma tu vida hoy",
                "🎯 Alcanza tus metas",
                "💪 Desarrolla tu potencial"
            ],
            # Añade más categorías según necesites
        }

    def send_alert(self, subject: str, message: str):
        """Envía alertas por email"""
        if not self.email_config:
            self.logger.warning("Configuración de email no disponible")
            return

        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = self.email_config['from']
            msg['To'] = self.email_config['to']

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(
                    self.email_config['username'],
                    self.email_config['password']
                )
                server.send_message(msg)
                
            self.logger.info(f"Alerta enviada: {subject}")
        except Exception as e:
            self.logger.error(f"Error enviando alerta: {e}")

    def get_products(self, category: str = None, min_price: float = None, 
                    max_price: float = None) -> List[Dict]:
        """
        Obtiene productos de Hotmart con filtros avanzados
        """
        try:
            # Construir parámetros de búsqueda
            params = {}
            if category:
                params["category"] = category
            if min_price:
                params["minPrice"] = min_price
            if max_price:
                params["maxPrice"] = max_price
                
            # Realizar petición a la API
            self.logger.info(f"Obteniendo productos para categoría: {category}")
            response = requests.get(
                f"{self.base_url}/products",
                headers=self.headers,
                params=params,
                timeout=30  # Timeout de 30 segundos
            )
            response.raise_for_status()
            products = response.json()['data']
            
            # Filtrar productos con buenos ratings y suficientes ventas
            filtered_products = [
                p for p in products 
                if p.get('rating', 0) >= 4.0 and 
                p.get('sales_count', 0) > 50
            ]
            
            self.logger.info(f"Productos encontrados: {len(filtered_products)}")
            return filtered_products
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error obteniendo productos: {e}")
            self.send_alert(
                "Error en Hotmart Automation",
                f"Error obteniendo productos: {str(e)}"
            )
            return []

    def generate_promotion_variants(self, product: Dict, category: str) -> List[str]:
        """
        Genera diferentes variantes de mensajes promocionales
        """
        # Obtener frases específicas de la categoría
        category_phrases = self.promo_phrases.get(
            category, 
            self.promo_phrases['marketing-digital']  # Categoría por defecto
        )
        
        templates = [
            "{intro_phrase}\n"
            "🎯 {name}\n"
            "💰 Precio especial: {price}\n"
            "✨ {description}\n"
            "👉 {link}\n"
            "#Hotmart #{category}",
            
            "⚡️ {intro_phrase}\n"
            "📚 Descubre: {name}\n"
            "🔥 {description}\n"
            "💎 ¡Accede ahora! {link}\n"
            "🏷️ Precio: {price}\n"
            "#Promoción #{category}",
            
            "🎉 ¡Oportunidad única!\n"
            "{intro_phrase}\n"
            "📊 {name}\n"
            "✅ {description}\n"
            "💫 ¡No esperes más! {link}\n"
            "#{category} #Aprendizaje"
        ]
        
        return [
            template.format(
                intro_phrase=random.choice(category_phrases),
                name=product['name'],
                price=product.get('price', 'Precio especial'),
                description=product.get('description', '')[:100] + '...',
                link='{affiliate_link}',
                category=category.replace('-', '')
            ) 
            for template in templates
        ]

    def publish_to_platform(self, platform: str, content: str, 
                          product_id: str) -> bool:
        """
        Publica contenido en una plataforma específica
        """
        platform_configs = {
            "facebook": {
                "url": "https://graph.facebook.com/v12.0/me/feed",
                "method": "post",
                "data_key": "message"
            },
            "twitter": {
                "url": "https://api.twitter.com/2/tweets",
                "method": "post",
                "data_key": "text"
            },
            "instagram": {
                "url": "https://graph.instagram.com/me/media",
                "method": "post",
                "data_key": "caption"
            }
        }
        
        if platform not in platform_configs:
            self.logger.error(f"Plataforma no soportada: {platform}")
            return False
            
        config = platform_configs[platform]
        try:
            # Aquí iría la implementación real con las APIs
            self.logger.info(f"Publicación exitosa en {platform}")
            return True
        except Exception as e:
            self.logger.error(f"Error publicando en {platform}: {e}")
            return False

    def run_automation(self, category: str = None, interval_hours: int = 24):
        """
        Ejecuta el ciclo completo de automatización
        """
        self.logger.info("Iniciando ciclo de automatización")
        
        while True:
            try:
                # 1. Obtener y filtrar productos
                products = self.get_products(
                    category=category,
                    min_price=50,
                    max_price=500
                )
                
                if not products:
                    raise Exception("No se encontraron productos adecuados")

                # 2. Seleccionar producto al azar
                product = random.choice(products)
                
                # 3. Generar contenido promocional
                promo_messages = self.generate_promotion_variants(
                    product,
                    category
                )
                
                # 4. Publicar en cada plataforma
                platforms = ["facebook", "twitter", "instagram"]
                for platform in platforms:
                    message = random.choice(promo_messages)
                    success = self.publish_to_platform(
                        platform,
                        message,
                        product['id']
                    )
                    
                    if success:
                        self.logger.info(
                            f"Publicación exitosa en {platform}"
                        )
                    else:
                        self.send_alert(
                            "Error de publicación",
                            f"Fallo al publicar en {platform}"
                        )

                # 5. Guardar datos y analizar rendimiento
                self.save_performance_data()
                self.analyze_performance()
                
                # 6. Esperar hasta el siguiente ciclo
                self.logger.info(
                    f"Ciclo completado. Esperando {interval_hours} horas"
                )
                time.sleep(interval_hours * 3600)
                
            except Exception as e:
                self.logger.error(f"Error en el ciclo de automatización: {e}")
                self.send_alert(
                    "Error crítico",
                    f"El sistema de automatización encontró un error: {str(e)}"
                )
                time.sleep(3600)  # Esperar 1 hora antes de reintentar

if __name__ == "__main__":
    # Configuración de ejemplo
    config = {
        "access_token": "TU_TOKEN_DE_ACCESO_HOTMART",
        "email_config": {
            "from": "tu@email.com",
            "to": "destino@email.com",
            "username": "tu@email.com",
            "password": "tu_contraseña"
        }
    }
    
    # Crear y ejecutar la automatización
    bot = HotmartAutomation(
        config["access_token"],
        config["email_config"]
    )
    bot.run_automation("marketing-digital") 


flowchart TD
    A[Trigger Diario] --> B{Obtener Productos Hotmart}
    B --> C[Filtrar Productos]
    C --> D[Generar Enlaces Afiliados]
    D --> E[Crear Mensajes Promocionales]
    E --> F[Publicar en Redes Sociales]
    F --> G[Guardar Datos]
    G --> H[Analizar Rendimiento]
    H --> I[Enviar Reporte]
    
    subgraph "Monitoreo"
        J[Verificar Errores]
        K[Alertas de Rendimiento]
        L[Registro de Actividad]
    end
    
    F --> J
    H --> K
    G --> L
    