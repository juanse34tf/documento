# Guía para Desarrollar el Taller de Programación II - Polimorfismo

Voy a ayudarte a entender cómo abordar cada etapa del taller sin darte directamente la solución, para que puedas aprender los conceptos de polimorfismo en Python.

## Etapa 1: Implementación Base del Sistema de Tarjetas

**Pasos a seguir:**

1. **Crear la Super Clase "Tarjeta"**:
    
    - Define una clase `Tarjeta` con un método inicializador (`__init__`) que reciba `id` y `saldo` (con valor default 0)
    - Implementa el método `pagar(cantidad)` que resta del saldo y muestra un mensaje
    - Implementa el método `mostrarSaldo()` que imprime el saldo actual
2. **Crear la Sub Clase "TarjetaDebito"**:
    
    - Hereda de la clase `Tarjeta` usando `class TarjetaDebito(Tarjeta):`
    - En esta etapa no necesita métodos adicionales, solo heredará los de la superclase
3. **Crear la Sub Clase "TarjetaCredito"**:
    
    - Hereda de la clase `Tarjeta`
    - Sobreescribe el método inicializador para incluir el descuento del 5%
    - Sobreescribe el método `pagar(cantidad)` para aplicar el descuento del 5%
4. **En la sección principal del código (fuera de las clases)**:
    
    - Crea un objeto `t1` de `TarjetaDebito` con ID y saldo inicial
    - Crea un objeto `t2` de `TarjetaCredito` con ID, saldo inicial y descuento
    - Realiza pagos con ambas tarjetas del mismo valor
    - Muestra el saldo de ambas tarjetas

## Etapa 2: Validación de longitud del ID

**Modificaciones a realizar:**

1. **Agregar el atributo `longitudId` a ambas subclases**:
    
    - En `TarjetaDebito`: Agrega `longitudId = 16` como atributo de clase
    - En `TarjetaCredito`: Agrega `longitudId = 16` como atributo de clase
2. **Modificar el método inicializador de la superclase**:
    
    - Verifica si la cantidad de dígitos del ID coincide con `self.__class__.longitudId`
    - Si la longitud no es correcta, muestra un mensaje de error
    - Usa `len(str(id))` para obtener la cantidad de dígitos
3. **En la sección principal del código**:
    
    - Crea un objeto `t1` de `TarjetaDebito` con ID de 10 dígitos
    - Crea un objeto `t2` de `TarjetaCredito` con ID de 16 dígitos

## Etapa 3: Implementación de manejo de excepciones

**Modificaciones a realizar:**

1. **Modificar el método inicializador de la superclase**:
    
    - Agrega validación de tipo para `id` y `saldo`
    - Usa `isinstance(id, str)` para verificar si es string
    - Lanza `TypeError` con mensaje apropiado si los tipos no son correctos
2. **Modificar el método `pagar` en ambas clases**:
    
    - Agrega validación de tipo para `cantidad`
    - Lanza `TypeError` si `cantidad` es un string
3. **En la sección principal del código**:
    
    - Usa bloques `try-except` para manejar las excepciones
    - Intenta crear un objeto `t1` con ID como string
    - Intenta crear un objeto `t2` con ID como entero
    - Intenta pagar con `t2` pasando un valor string
    - Intenta pagar con `t1` pasando un valor entero

## Estructura general de cada archivo

Para cada archivo (.py) te recomiendo seguir esta estructura:

```python
# Nombre: Tu Nombre Completo
# Fecha: April 18, 2025
# Asignatura: Programación II
# Taller 2: Etapa X

# Definición de clases

# Código principal de ejecución

# Análisis del polimorfismo (en comentarios)
```

Recuerda que el objetivo principal es entender cómo el polimorfismo permite que diferentes objetos respondan de manera distinta al mismo mensaje (llamado a método), adaptando su comportamiento según la clase a la que pertenecen.