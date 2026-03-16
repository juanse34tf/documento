def calcular_todo(secuencia, ordenes, matriz):
    t_prod = 0
    t_setup = 0
    penalidad = 0
    consumo = 0
    cambios = 0
    
    for i in range(len(secuencia)):
        cod = secuencia[i]
        
        orden_actual = None
        for o in ordenes:
            if o["codigo"] == cod:
                orden_actual = o
                break
        
        t_prod = t_prod + (orden_actual["cantidad"] * orden_actual["t_unit"]) / 60
        consumo = consumo + (orden_actual["cantidad"] / 1000) * orden_actual["cons"]
        
        if i > 0:
            cod_ant = secuencia[i-1]
            orden_ant = None
            for o in ordenes:
                if o["codigo"] == cod_ant:
                    orden_ant = o
                    break
                    
            mat1 = orden_ant["mat"] - 1
            mat2 = orden_actual["mat"] - 1
            
            if mat1 != mat2:
                setup = matriz[mat1][mat2]
                t_setup = t_setup + setup
                cambios = cambios + 1
            else:
                setup = 0
                
            if orden_actual["prio"] == 5:
                mal_ubicado = False
                for j in range(i):
                    cod_viejo = secuencia[j]
                    orden_vieja = None
                    for o in ordenes:
                        if o["codigo"] == cod_viejo:
                            orden_vieja = o
                            break
                    if orden_vieja["prio"] <= 3:
                        mal_ubicado = True
                
                if mal_ubicado == True:
                    if setup > 25:
                        penalidad = penalidad + 10
                    else:
                        penalidad = penalidad + 50
                        
    costo = t_prod + t_setup + penalidad
    
    return t_prod, t_setup, penalidad, costo, cambios, consumo