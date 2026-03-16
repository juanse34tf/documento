# Sistema de Alertas de Inventario con n8n

## 📋 Descripción del Sistema

Este flujo automatizado monitorea un archivo Excel en Google Drive cada 30 minutos. Cuando detecta que el inventario de papel está por debajo de 10 unidades, genera automáticamente una alerta de voz y realiza una llamada VoIP usando Asterisk.

## 🏗️ Arquitectura del Sistema

```
[Google Drive Excel] 
        ↓ (cada 30 min)
[n8n Workflow] 
        ↓ (si papel < 10)
[Python Script + gTTS] 
        ↓ (genera MP3)
[Asterisk PBX] 
        ↓ (realiza llamada)
[SoftPhone/Teléfono] (reproduce audio)

[FastAPI] → [n8n Webhook] (activación manual)
```

## 🛠️ Componentes del Sistema

1. **n8n Workflow**: Orquestación principal del proceso
2. **Google Drive Integration**: Acceso al archivo Excel de inventario
3. **gTTS (Google Text-to-Speech)**: Generación de audio
4. **Asterisk PBX**: Sistema de llamadas VoIP
5. **FastAPI**: Endpoint para activación manual
6. **Python Scripts**: Lógica de procesamiento

## 🎯 Funcionalidades Principales

1. **Monitoreo Automático**: Revisa el Excel cada 30 minutos
2. **Detección Inteligente**: Identifica cuando papel < 10 unidades
3. **Generación de Voz**: Crea archivos MP3 con gTTS
4. **Llamadas VoIP**: Usa Asterisk para llamadas automáticas
5. **Activación Manual**: API FastAPI para triggers externos
6. **Escalamiento**: Múltiples números de respaldo
7. **Logs Completos**: Monitoreo y auditoría

---

## 📄 n8n Workflow JSON

```json
{
  "name": "Inventario - Alerta de Voz Automática",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "minutes",
              "minutesInterval": 30
            }
          ]
        }
      },
      "id": "cron-trigger",
      "name": "Cron - Cada 30 minutos",
      "type": "n8n-nodes-base.cron",
      "typeVersion": 1,
      "position": [240, 300]
    },
    {
      "parameters": {
        "authentication": "oAuth2Api",
        "resource": "file",
        "operation": "download",
        "fileId": "={{ $env.INVENTORY_FILE_ID }}",
        "options": {}
      },
      "id": "google-drive-node",
      "name": "Google Drive - Descargar Excel",
      "type": "n8n-nodes-base.googleDrive",
      "typeVersion": 3,
      "position": [460, 300]
    },
    {
      "parameters": {
        "operation": "read",
        "binaryPropertyName": "data",
        "options": {
          "headerRow": 0,
          "range": "A:C"
        }
      },
      "id": "spreadsheet-node",
      "name": "Leer Excel - Inventario",
      "type": "n8n-nodes-base.spreadsheetFile",
      "typeVersion": 2,
      "position": [680, 300]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "papel-condition",
              "leftValue": "={{ $json.papel }}",
              "rightValue": 10,
              "operator": {
                "type": "number",
                "operation": "lt"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "if-node",
      "name": "IF - Papel < 10",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [900, 300]
    },
    {
      "parameters": {
        "command": "python3 /opt/n8n/scripts/generate_voice_alert.py",
        "options": {}
      },
      "id": "python-voice-node",
      "name": "Python - Generar Audio",
      "type": "n8n-nodes-base.executeCommand",
      "typeVersion": 1,
      "position": [1120, 200]
    },
    {
      "parameters": {
        "command": "asterisk -rx \"originate Local/alert@internal extension alert@voip-alerts\"",
        "options": {}
      },
      "id": "asterisk-call-node",
      "name": "Asterisk - Realizar Llamada",
      "type": "n8n-nodes-base.executeCommand",
      "typeVersion": 1,
      "position": [1340, 200]
    },
    {
      "parameters": {
        "httpMethod": "POST",
        "path": "inventory-alert",
        "options": {}
      },
      "id": "webhook-manual",
      "name": "Webhook - Activación Manual",
      "type": "n8n-nodes-base.webhook",
      "typeVersion": 2,
      "position": [240, 500]
    },
    {
      "parameters": {
        "conditions": {
          "options": {
            "caseSensitive": true,
            "leftValue": "",
            "typeValidation": "strict"
          },
          "conditions": [
            {
              "id": "manual-trigger",
              "leftValue": "={{ $json.action }}",
              "rightValue": "manual_alert",
              "operator": {
                "type": "string",
                "operation": "equals"
              }
            }
          ],
          "combinator": "and"
        },
        "options": {}
      },
      "id": "if-manual-node",
      "name": "IF - Activación Manual",
      "type": "n8n-nodes-base.if",
      "typeVersion": 2,
      "position": [460, 500]
    },
    {
      "parameters": {
        "command": "python3 /opt/n8n/scripts/generate_voice_alert.py --manual",
        "options": {}
      },
      "id": "python-manual-node",
      "name": "Python - Audio Manual",
      "type": "n8n-nodes-base.executeCommand",
      "typeVersion": 1,
      "position": [680, 500]
    },
    {
      "parameters": {
        "command": "asterisk -rx \"originate Local/manual@internal extension alert@voip-alerts\"",
        "options": {}
      },
      "id": "asterisk-manual-node",
      "name": "Asterisk - Llamada Manual",
      "type": "n8n-nodes-base.executeCommand",
      "typeVersion": 1,
      "position": [900, 500]
    }
  ],
  "connections": {
    "Cron - Cada 30 minutos": {
      "main": [
        [
          {
            "node": "Google Drive - Descargar Excel",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Google Drive - Descargar Excel": {
      "main": [
        [
          {
            "node": "Leer Excel - Inventario",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Leer Excel - Inventario": {
      "main": [
        [
          {
            "node": "IF - Papel < 10",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF - Papel < 10": {
      "main": [
        [
          {
            "node": "Python - Generar Audio",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Python - Generar Audio": {
      "main": [
        [
          {
            "node": "Asterisk - Realizar Llamada",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Webhook - Activación Manual": {
      "main": [
        [
          {
            "node": "IF - Activación Manual",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF - Activación Manual": {
      "main": [
        [
          {
            "node": "Python - Audio Manual",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "Python - Audio Manual": {
      "main": [
        [
          {
            "node": "Asterisk - Llamada Manual",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "pinData": {},
  "settings": {
    "executionOrder": "v1"
  },
  "staticData": null,
  "tags": [],
  "triggerCount": 2,
  "updatedAt": "2025-07-30T12:00:00.000Z",
  "versionId": "1"
}
```

---

## 🐍 Script Python - Generador de Audio

**Ubicación**: `/opt/n8n/scripts/generate_voice_alert.py`

```python
#!/usr/bin/env python3
"""
Script para generar alertas de voz usando gTTS
Ubicación: /opt/n8n/scripts/generate_voice_alert.py
"""

import os
import sys
import argparse
from gtts import gTTS
from datetime import datetime
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/n8n/voice_alerts.log'),
        logging.StreamHandler()
    ]
)

def generate_voice_alert(message, output_path, language='es'):
    """
    Genera un archivo de audio MP3 usando gTTS
    
    Args:
        message (str): Texto a convertir en voz
        output_path (str): Ruta donde guardar el archivo MP3
        language (str): Idioma para la síntesis de voz
    """
    try:
        # Crear objeto gTTS
        tts = gTTS(text=message, lang=language, slow=False)
        
        # Guardar archivo
        tts.save(output_path)
        
        logging.info(f"Audio generado exitosamente: {output_path}")
        return True
        
    except Exception as e:
        logging.error(f"Error generando audio: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Generar alerta de voz para inventario')
    parser.add_argument('--manual', action='store_true', help='Activación manual')
    parser.add_argument('--message', type=str, help='Mensaje personalizado')
    parser.add_argument('--output', type=str, help='Archivo de salida')
    
    args = parser.parse_args()
    
    # Configurar directorios
    audio_dir = "/var/spool/asterisk/sounds/custom"
    os.makedirs(audio_dir, exist_ok=True)
    
    # Definir mensaje
    if args.message:
        message = args.message
    elif args.manual:
        message = "Hola, esta es una prueba de alerta manual del sistema de inventario."
    else:
        message = "Hola, se ha detectado que el inventario de papel está bajo. Por favor revisa."
    
    # Definir archivo de salida
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if args.output:
        output_file = args.output
    else:
        filename = f"inventory_alert_{timestamp}.mp3"
        output_file = os.path.join(audio_dir, filename)
    
    # Generar audio
    success = generate_voice_alert(message, output_file)
    
    if success:
        print(f"SUCCESS:{output_file}")
        logging.info(f"Alerta de voz generada: {output_file}")
        
        # Crear symlink para Asterisk
        asterisk_file = os.path.join(audio_dir, "current_alert.mp3")
        if os.path.exists(asterisk_file):
            os.remove(asterisk_file)
        os.symlink(output_file, asterisk_file)
        
        return 0
    else:
        print("ERROR: No se pudo generar el audio")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## ☎️ Configuración Asterisk

**Ubicación**: `/etc/asterisk/extensions.conf`

```conf
;
; Configuración Asterisk para alertas de inventario
; Ubicación: /etc/asterisk/extensions.conf
;

[general]
static=yes
writeprotect=no
clearglobalvars=no

[globals]
; Variables globales
ALERT_PHONE=1000  ; Extensión o número a llamar
AUDIO_PATH=/var/spool/asterisk/sounds/custom

[internal]
; Contexto para llamadas internas

; Extensión para alertas automáticas
exten => alert,1,NoOp(=== INICIANDO ALERTA DE INVENTARIO ===)
 same => n,Set(CHANNEL(hangup_handler_push)=hangup-handler,s,1)
 same => n,Answer()
 same => n,Wait(1)
 same => n,Playback(${AUDIO_PATH}/current_alert)
 same => n,Wait(2)
 same => n,Playback(${AUDIO_PATH}/current_alert)  ; Repetir mensaje
 same => n,Wait(1)
 same => n,Hangup()

; Extensión para alertas manuales
exten => manual,1,NoOp(=== ALERTA MANUAL DE INVENTARIO ===)
 same => n,Set(CHANNEL(hangup_handler_push)=hangup-handler,s,1)
 same => n,Answer()
 same => n,Wait(1)
 same => n,Playback(${AUDIO_PATH}/current_alert)
 same => n,Wait(1)
 same => n,Hangup()

[voip-alerts]
; Contexto para extensiones que reciben alertas

; Extensión principal de alertas
exten => alert,1,NoOp(=== RECIBIENDO ALERTA ===)
 same => n,Dial(SIP/${ALERT_PHONE},30,tT)
 same => n,GotoIf($["${DIALSTATUS}" = "ANSWER"]?answered:noanswer)
 same => n(answered),NoOp(Llamada contestada)
 same => n,Hangup()
 same => n(noanswer),NoOp(No se contestó la llamada)
 same => n,System(echo "$(date): Alerta no contestada" >> /var/log/asterisk/alerts.log)
 same => n,Hangup()

[hangup-handler]
; Manejador de colgado
exten => s,1,NoOp(=== LLAMADA FINALIZADA ===)
 same => n,System(echo "$(date): Alerta completada" >> /var/log/asterisk/alerts.log)
 same => n,Return()

; Extensión de prueba
[test-context]
exten => test,1,NoOp(=== PRUEBA DE SISTEMA ===)
 same => n,Answer()
 same => n,Playback(hello-world)
 same => n,Hangup()

; Configuración para SoftPhone local
[softphone]
exten => 1000,1,NoOp(=== SOFTPHONE LOCAL ===)
 same => n,Dial(SIP/1000,20)
 same => n,Hangup()
```

---

## 🚀 FastAPI - Endpoint Manual

**Ubicación**: `/opt/n8n/api/manual_trigger.py`

```python
#!/usr/bin/env python3
"""
FastAPI endpoint para activar alertas manuales
Ubicación: /opt/n8n/api/manual_trigger.py
"""

from fastapi import FastAPI, HTTPException, BackgroundTasks
from pydantic import BaseModel
import requests
import logging
import os
from datetime import datetime
from typing import Optional

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Sistema de Alertas de Inventario",
    description="API para activar alertas manuales del sistema de inventario",
    version="1.0.0"
)

# Configuración
N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', 'http://localhost:5678/webhook/inventory-alert')
N8N_API_KEY = os.getenv('N8N_API_KEY', '')

class AlertRequest(BaseModel):
    action: str = "manual_alert"
    message: Optional[str] = None
    phone_number: Optional[str] = None
    urgency: Optional[str] = "normal"  # normal, high, critical

class AlertResponse(BaseModel):
    success: bool
    message: str
    timestamp: str
    alert_id: Optional[str] = None

def trigger_n8n_workflow(alert_data: dict) -> bool:
    """
    Dispara el workflow de n8n a través del webhook
    """
    try:
        headers = {
            'Content-Type': 'application/json'
        }
        
        if N8N_API_KEY:
            headers['Authorization'] = f'Bearer {N8N_API_KEY}'
        
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=alert_data,
            headers=headers,
            timeout=30
        )
        
        response.raise_for_status()
        logger.info(f"Workflow n8n activado exitosamente: {response.status_code}")
        return True
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error activando workflow n8n: {str(e)}")
        return False

@app.get("/")
async def root():
    """Endpoint raíz con información de la API"""
    return {
        "message": "Sistema de Alertas de Inventario",
        "version": "1.0.0",
        "endpoints": {
            "manual_alert": "/alert/manual",
            "health": "/health",
            "status": "/status"
        }
    }

@app.get("/health")
async def health_check():
    """Verificación de salud del servicio"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "inventory-alerts-api"
    }

@app.post("/alert/manual", response_model=AlertResponse)
async def trigger_manual_alert(
    alert_request: AlertRequest,
    background_tasks: BackgroundTasks
):
    """
    Activar una alerta manual del sistema de inventario
    """
    try:
        alert_id = f"manual_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        # Preparar datos para n8n
        alert_data = {
            "action": alert_request.action,
            "alert_id": alert_id,
            "timestamp": datetime.now().isoformat(),
            "message": alert_request.message,
            "phone_number": alert_request.phone_number,
            "urgency": alert_request.urgency,
            "source": "manual_api"
        }
        
        # Activar workflow en background
        success = trigger_n8n_workflow(alert_data)
        
        if success:
            logger.info(f"Alerta manual activada: {alert_id}")
            return AlertResponse(
                success=True,
                message="Alerta manual activada exitosamente",
                timestamp=datetime.now().isoformat(),
                alert_id=alert_id
            )
        else:
            raise HTTPException(
                status_code=500,
                detail="Error activando el workflow de n8n"
            )
            
    except Exception as e:
        logger.error(f"Error en alerta manual: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error interno del servidor: {str(e)}"
        )

@app.post("/alert/test")
async def test_alert():
    """
    Alerta de prueba para verificar el sistema
    """
    test_request = AlertRequest(
        action="manual_alert",
        message="Esta es una prueba del sistema de alertas de inventario",
        urgency="normal"
    )
    
    return await trigger_manual_alert(test_request, BackgroundTasks())

if __name__ == "__main__":
    import uvicorn
    
    # Configuración del servidor
    port = int(os.getenv('PORT', 8000))
    host = os.getenv('HOST', '0.0.0.0')
    
    logger.info(f"Iniciando servidor en {host}:{port}")
    
    uvicorn.run(
        "manual_trigger:app",
        host=host,
        port=port,
        reload=True,
        log_level="info"
    )
```

---

## 📦 Instalación y Configuración

### Requisitos Previos
```bash
# Instalar n8n
npm install -g n8n

# Instalar Asterisk
sudo apt-get install asterisk asterisk-modules

# Instalar Python y dependencias
sudo apt-get install python3 python3-pip
pip3 install gtts fastapi uvicorn requests pydantic
```

### Configuración de Directorios
```bash
# Crear directorios necesarios
sudo mkdir -p /opt/n8n/scripts
sudo mkdir -p /opt/n8n/api
sudo mkdir -p /var/log/n8n
sudo mkdir -p /var/spool/asterisk/sounds/custom

# Permisos
sudo chown -R n8n:n8n /opt/n8n/
sudo chmod +x /opt/n8n/scripts/generate_voice_alert.py
```

### Variables de Entorno
```bash
# Variables para n8n (.env)
INVENTORY_FILE_ID=your_google_drive_file_id_here
N8N_WEBHOOK_URL=http://localhost:5678/webhook/inventory-alert
N8N_API_KEY=your_n8n_api_key_here
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json
```

### Estructura del Archivo Excel
El archivo de inventario debe tener la siguiente estructura:

| Producto | Cantidad | Unidad |
|----------|----------|--------|
| papel    | 8        | Cajas  |
| tinta    | 15       | Cartuchos |

**Importante**: La columna de papel debe llamarse exactamente "papel".

---

## 🧪 Pruebas del Sistema

### Prueba Manual del Script Python
```bash
# Generar audio de prueba
python3 /opt/n8n/scripts/generate_voice_alert.py --manual

# Verificar archivo generado
ls -la /var/spool/asterisk/sounds/custom/
```

### Prueba de Asterisk
```bash
# Conectar a consola Asterisk
sudo asterisk -r

# Ejecutar prueba
originate Local/test@test-context extension test@test-context
```

### Prueba del API
```bash
# Prueba básica
curl -X GET http://localhost:8000/health

# Activar alerta manual
curl -X POST http://localhost:8000/alert/manual \
  -H "Content-Type: application/json" \
  -d '{"action": "manual_alert", "urgency": "normal"}'
```

---

## 📊 Monitoreo y Logs

### Ubicaciones de Logs
```bash
# Logs de n8n
tail -f ~/.n8n/logs/n8n.log

# Logs del script Python
tail -f /var/log/n8n/voice_alerts.log

# Logs de Asterisk
tail -f /var/log/asterisk/full
tail -f /var/log/asterisk/alerts.log

# Logs de FastAPI
journalctl -u inventory-alerts-api -f
```

### Comandos de Diagnóstico
```bash
# Estado de servicios
sudo systemctl status asterisk
sudo systemctl status inventory-alerts-api

# Verificar conectividad n8n
curl -X GET http://localhost:5678/webhook-test/inventory-alert

# Test de audio
play /var/spool/asterisk/sounds/custom/current_alert.mp3
```

---

## 🛡️ Solución de Problemas

### Problemas Comunes

**Error: "No se puede acceder a Google Drive"**
- Verificar credenciales OAuth 2.0
- Comprobar permisos del archivo
- Revisar tokens de acceso

**Error: "gTTS no funciona"**
- Verificar conexión a internet
- Instalar dependencias: `pip3 install gtts`
- Comprobar permisos de directorio

**Error: "Asterisk no responde"**
- Verificar estado: `sudo systemctl status asterisk`
- Revisar configuración: `/etc/asterisk/extensions.conf`
- Comprobar puertos: `netstat -tulpn | grep asterisk`

### Comandos de Limpieza
```bash
# Limpiar archivos de audio antiguos
find /var/spool/asterisk/sounds/custom/ -name "inventory_alert_*.mp3" -mtime +7 -delete

# Reiniciar servicios si hay problemas
sudo systemctl restart asterisk
sudo systemctl restart inventory-alerts-api
n8n restart
```

---

## 📈 Características Avanzadas

### Funcionalidades Adicionales
1. **Múltiples Productos**: Extender para monitorear varios productos
2. **Diferentes Umbrales**: Configurar umbrales por producto
3. **Escalamiento**: Llamadas a múltiples números
4. **SMS Backup**: Enviar SMS si la llamada falla
5. **Dashboard**: Interfaz web para monitoreo
6. **Historial**: Base de datos de alertas

### Escalamiento de Llamadas
```conf
; En extensions.conf
exten => alert,1,NoOp(=== ALERTA CON ESCALAMIENTO ===)
 same => n,Dial(SIP/1000,20)
 same => n,GotoIf($["${DIALSTATUS}" = "ANSWER"]?answered:try_backup)
 same => n(try_backup),Dial(SIP/1001,20)
 same => n,GotoIf($["${DIALSTATUS}" = "ANSWER"]?answered:try_emergency)
 same => n(try_emergency),Dial(SIP/1002,20)
 same => n(answered),Playback(${AUDIO_PATH}/current_alert)
 same => n,Hangup()
```

---

## 🎯 README Simplificado para IA

### OBJETIVO
Sistema automatizado que monitorea Excel en Google Drive cada 30 min. Si papel < 10 unidades → genera MP3 con gTTS → realiza llamada VoIP con Asterisk.

### INSTALACIÓN
```bash
npm install -g n8n
sudo apt install asterisk python3-pip
pip3 install gtts fastapi uvicorn
sudo mkdir -p /opt/n8n/{scripts,api} /var/spool/asterisk/sounds/custom
```

### CONFIGURACIÓN
```bash
INVENTORY_FILE_ID=google_drive_file_id
N8N_WEBHOOK_URL=http://localhost:5678/webhook/inventory-alert
```

### PRUEBAS
```bash
# Probar Python
python3 /opt/n8n/scripts/generate_voice_alert.py --manual

# Probar API
curl -X POST http://localhost:8000/alert/manual

# Verificar audio
ls /var/spool/asterisk/sounds/custom/
```

### ARCHIVOS CLAVE
```
/opt/n8n/scripts/generate_voice_alert.py  # Audio generator
/opt/n8n/api/manual_trigger.py            # Manual API
/etc/asterisk/extensions.conf             # Call routing
/var/spool/asterisk/sounds/custom/        # Audio files
```

---

## 📋 Checklist de Implementación

### Pre-implementación
- [ ] Servidor configurado con todos los componentes
- [ ] Credenciales de Google Drive obtenidas
- [ ] Archivo Excel de inventario creado
- [ ] Asterisk instalado y configurado
- [ ] Python y dependencias instaladas

### Implementación
- [ ] Flujo n8n importado y configurado
- [ ] Scripts Python instalados y probados
- [ ] API FastAPI funcionando
- [ ] Asterisk configurado para llamadas
- [ ] Webhooks configurados

### Post-implementación
- [ ] Pruebas completas realizadas
- [ ] Logs configurados y funcionando
- [ ] Monitoreo activo
- [ ] Documentación actualizada

---

## 🏷️ Tags

#n8n #automatización #asterisk #voip #gTTS #fastapi #python #inventario #alertas #google-drive #excel #monitoreo #llamadas #audio #sistema-alertas


---

## 🌐 Instalación en Oracle Cloud Free Tier

### Script de Instalación Automática

```bash
#!/bin/bash
# install_inventory_system.sh
# Script para instalar el sistema completo en Oracle Cloud

echo "=== INSTALANDO SISTEMA DE ALERTAS DE INVENTARIO ==="

# Variables
N8N_USER="n8n"
N8N_HOME="/home/$N8N_USER"

# Actualizar sistema
echo "Actualizando sistema..."
sudo apt update && sudo apt upgrade -y

# Instalar dependencias principales
echo "Instalando dependencias..."
sudo apt install -y curl wget git python3-pip nodejs npm asterisk ufw

# Instalar n8n globalmente
echo "Instalando n8n..."
sudo npm install -g n8n

# Crear usuario para n8n
echo "Creando usuario n8n..."
sudo useradd -m -s /bin/bash $N8N_USER
sudo usermod -aG sudo $N8N_USER

# Instalar dependencias Python
echo "Instalando dependencias Python..."
pip3 install gtts fastapi uvicorn requests pydantic

# Crear estructura de directorios
echo "Creando directorios..."
sudo mkdir -p /opt/n8n/{scripts,api,logs}
sudo mkdir -p /var/spool/asterisk/sounds/custom
sudo mkdir -p /var/log/n8n

# Configurar permisos
sudo chown -R $N8N_USER:$N8N_USER /opt/n8n/
sudo chown -R asterisk:asterisk /var/spool/asterisk/
sudo chmod 755 /opt/n8n/scripts/
sudo chmod 755 /opt/n8n/api/

# Configurar firewall
echo "Configurando firewall..."
sudo ufw allow 22/tcp      # SSH
sudo ufw allow 5678/tcp    # n8n
sudo ufw allow 8000/tcp    # FastAPI
sudo ufw allow 5060/udp    # SIP
sudo ufw --force enable

# Crear archivos del sistema
echo "Creando archivos del sistema..."

# Script Python
sudo tee /opt/n8n/scripts/generate_voice_alert.py > /dev/null << 'EOF'
#!/usr/bin/env python3
import os, sys, argparse
from gtts import gTTS
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_voice_alert(message, output_path, language='es'):
    try:
        tts = gTTS(text=message, lang=language, slow=False)
        tts.save(output_path)
        logging.info(f"Audio generado: {output_path}")
        return True
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--manual', action='store_true')
    parser.add_argument('--message', type=str)
    args = parser.parse_args()
    
    audio_dir = "/var/spool/asterisk/sounds/custom"
    os.makedirs(audio_dir, exist_ok=True)
    
    if args.message:
        message = args.message
    elif args.manual:
        message = "Esta es una prueba del sistema de alertas"
    else:
        message = "Inventario de papel está bajo. Por favor revisar."
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(audio_dir, f"alert_{timestamp}.mp3")
    
    if generate_voice_alert(message, output_file):
        current_alert = os.path.join(audio_dir, "current_alert.mp3")
        if os.path.exists(current_alert):
            os.remove(current_alert)
        os.symlink(output_file, current_alert)
        print(f"SUCCESS:{output_file}")
        return 0
    else:
        print("ERROR")
        return 1

if __name__ == "__main__":
    sys.exit(main())
EOF

# API FastAPI
sudo tee /opt/n8n/api/manual_trigger.py > /dev/null << 'EOF'
#!/usr/bin/env python3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests, os, logging
from datetime import datetime

app = FastAPI(title="Sistema de Alertas")
N8N_WEBHOOK_URL = os.getenv('N8N_WEBHOOK_URL', 'http://localhost:5678/webhook/inventory-alert')

class AlertRequest(BaseModel):
    action: str = "manual_alert"
    message: str = None
    urgency: str = "normal"

@app.get("/")
async def root():
    return {"message": "Sistema de Alertas de Inventario", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

@app.post("/alert/manual")
async def manual_alert(request: AlertRequest):
    try:
        alert_data = {
            "action": request.action,
            "timestamp": datetime.now().isoformat(),
            "message": request.message,
            "urgency": request.urgency
        }
        
        response = requests.post(N8N_WEBHOOK_URL, json=alert_data, timeout=10)
        
        if response.status_code == 200:
            return {"success": True, "message": "Alerta activada"}
        else:
            raise HTTPException(status_code=500, detail="Error en n8n")
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/alert/test")
async def test_alert():
    return await manual_alert(AlertRequest(message="Prueba del sistema"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
EOF

# Configuración básica de Asterisk
sudo tee /etc/asterisk/extensions.conf > /dev/null << 'EOF'
[general]
static=yes
writeprotect=no

[globals]
AUDIO_PATH=/var/spool/asterisk/sounds/custom

[internal]
exten => alert,1,NoOp(ALERTA DE INVENTARIO)
 same => n,Answer()
 same => n,Wait(1)
 same => n,Playback(${AUDIO_PATH}/current_alert)
 same => n,Wait(1)
 same => n,Hangup()

[demo]
exten => test,1,Answer()
 same => n,Playback(demo-congrats)
 same => n,Hangup()
EOF

# Hacer ejecutables
sudo chmod +x /opt/n8n/scripts/generate_voice_alert.py
sudo chmod +x /opt/n8n/api/manual_trigger.py

# Crear servicios systemd
sudo tee /etc/systemd/system/inventory-api.service > /dev/null << EOF
[Unit]
Description=Inventory Alerts API
After=network.target

[Service]
Type=simple
User=$N8N_USER
WorkingDirectory=/opt/n8n/api
ExecStart=/usr/bin/python3 manual_trigger.py
Restart=always
Environment=N8N_WEBHOOK_URL=http://localhost:5678/webhook/inventory-alert

[Install]
WantedBy=multi-user.target
EOF

sudo tee /etc/systemd/system/n8n.service > /dev/null << EOF
[Unit]
Description=n8n workflow automation
After=network.target

[Service]
Type=simple
User=$N8N_USER
ExecStart=/usr/local/bin/n8n start
WorkingDirectory=$N8N_HOME
Environment=N8N_HOST=0.0.0.0
Environment=N8N_PORT=5678
Environment=N8N_PROTOCOL=http
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# Habilitar servicios
sudo systemctl daemon-reload
sudo systemctl enable asterisk
sudo systemctl enable inventory-api
sudo systemctl enable n8n

# Iniciar servicios
echo "Iniciando servicios..."
sudo systemctl start asterisk
sudo systemctl start inventory-api

# Configurar n8n como usuario n8n
echo "Configurando n8n..."
sudo -u $N8N_USER bash -c "cd $N8N_HOME && n8n start &"
sleep 10
sudo pkill -f n8n

sudo systemctl start n8n

# Mostrar información final
echo ""
echo "=== INSTALACIÓN COMPLETADA ==="
echo "n8n: http://$(curl -s ifconfig.me):5678"
echo "API: http://$(curl -s ifconfig.me):8000"
echo "SSH: ssh ubuntu@$(curl -s ifconfig.me)"
echo ""
echo "Servicios:"
sudo systemctl status asterisk --no-pager -l
sudo systemctl status inventory-api --no-pager -l
sudo systemctl status n8n --no-pager -l
echo ""
echo "Para probar:"
echo "curl http://$(curl -s ifconfig.me):8000/health"
echo "curl -X POST http://$(curl -s ifconfig.me):8000/alert/test"
```

### Comandos de Configuración Post-Instalación

```bash
# Ejecutar el script
chmod +x install_inventory_system.sh
./install_inventory_system.sh

# Configurar dominio (opcional)
# En Oracle Cloud Console: Networking > DNS Management
# Agregar registro A: alerts.tu-dominio.com -> IP_PUBLICA

# Configurar SSL con Let's Encrypt
sudo apt install certbot nginx -y
sudo nginx -t
sudo certbot --nginx -d alerts.tu-dominio.com
```

### Configuración de Seguridad en Oracle Cloud

```bash
# En Oracle Console: Networking > Security Lists
# Agregar reglas de ingreso:

# HTTP/HTTPS
0.0.0.0/0 TCP 80
0.0.0.0/0 TCP 443

# n8n (temporal para demo)
0.0.0.0/0 TCP 5678

# API
0.0.0.0/0 TCP 8000

# SIP (si necesitas VoIP externo)
0.0.0.0/0 UDP 5060
```

### Script de Demo Automatizada

```bash
#!/bin/bash
# demo_sistema.sh - Script para mostrar el sistema funcionando

echo "=== DEMO SISTEMA DE ALERTAS DE INVENTARIO ==="

# Verificar servicios
echo "1. Verificando servicios..."
curl -s http://localhost:8000/health | jq '.'

# Crear archivo Excel de prueba
echo "2. Simulando archivo Excel con inventario bajo..."
python3 << EOF
import json
data = [{"producto": "papel", "cantidad": 5, "unidad": "Cajas"}]
print("Inventario actual:", json.dumps(data, indent=2))
EOF

# Generar alerta de prueba
echo "3. Generando alerta de voz..."
python3 /opt/n8n/scripts/generate_voice_alert.py --message "Demo: Inventario de papel está bajo, solo quedan 5 cajas"

# Verificar archivo de audio
echo "4. Verificando archivo de audio generado..."
ls -la /var/spool/asterisk/sounds/custom/

# Probar API
echo "5. Probando API de alertas manuales..."
curl -X POST http://localhost:8000/alert/test \
  -H "Content-Type: application/json" | jq '.'

# Mostrar métricas
echo "6. Métricas del sistema..."
echo "Uptime: $(uptime)"
echo "Memoria: $(free -h | grep Mem)"
echo "Disco: $(df -h | grep '/dev')"

echo ""
echo "=== DEMO COMPLETADA ==="
echo "Acceso web: http://$(curl -s ifconfig.me):5678"
echo "API docs: http://$(curl -s ifconfig.me):8000/docs"
```
