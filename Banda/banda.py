def leer_Infrarojo():
    botella_detectada = True
    return botella_detectada

def leer_sensor_nivel():
    nivel_liquido = 95
    return nivel_liquido

def dejar_pasar():
    print("Botella OK")

def activar_piston_rechazo():
    print("Botella defectuosa")

def contar_error():
    print("Error contabilizado")

banda_activa = True

while banda_activa == True:
    botella_detectada = leer_Infrarojo()
    
    if botella_detectada:
        nivel_liquido = leer_sensor_nivel()
        
        if nivel_liquido >= 90:
            dejar_pasar()
        else:
            activar_piston_rechazo()
            contar_error()




