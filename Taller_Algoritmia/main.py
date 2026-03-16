codigos =     ["101",  "102",  "103",  "104",  "105",  "106",  "107",  "108",  "109",  "110"]
cantidades =  [5000,   3000,   4500,   2000,   3500,   2500,   4000,   1500,   3800,   2200]
tiempos =     [2.5,    3.0,    2.8,    4.0,    3.2,    3.5,    2.6,    4.5,    3.1,    3.8]
materiales =  [1,      2,      1,      3,      2,      3,      1,      3,      2,      1]
prioridades = [3,      5,      2,      4,      1,      5,      4,      2,      3,      5]
consumos =    [120,    150,    110,    180,    140,    200,    115,    210,    130,    125]

matriz = [
    [0, 18, 32],
    [20, 0, 27],
    [35, 22, 0]
]

secuencia = ["110", "102", "106", "104", "107", "101", "103", "109", "105", "108"]

t_prod = 0
t_setup = 0
penalidad = 0
consumo = 0
cambios = 0

for i in range(len(secuencia)):
    pos = -1
    for j in range(len(codigos)):
        if codigos[j] == secuencia[i]:
            pos = j
            break

    t_prod = t_prod + (cantidades[pos] * tiempos[pos]) / 60
    consumo = consumo + (cantidades[pos] / 1000) * consumos[pos]

    if i > 0:
        pos_ant = -1
        for j in range(len(codigos)):
            if codigos[j] == secuencia[i - 1]:
                pos_ant = j
                break

        mat1 = materiales[pos_ant] - 1
        mat2 = materiales[pos] - 1

        if mat1 != mat2:
            setup = matriz[mat1][mat2]
            t_setup = t_setup + setup
            cambios = cambios + 1
        else:
            setup = 0

        if prioridades[pos] == 5:
            mal_ubicado = False
            for k in range(i):
                pos_viejo = -1
                for j in range(len(codigos)):
                    if codigos[j] == secuencia[k]:
                        pos_viejo = j
                        break
                if prioridades[pos_viejo] <= 3:
                    mal_ubicado = True

            if mal_ubicado == True:
                if setup > 25:
                    penalidad = penalidad + 10
                else:
                    penalidad = penalidad + 50

costo = t_prod + t_setup + penalidad

print("1. Secuencia final:", secuencia)
print("2. Tiempo de produccion total (min):", round(t_prod, 2))
print("3. Tiempo total de setups (min):", t_setup)
print("4. Penalizacion total (min):", penalidad)
print("5. Costo total final (min):", round(costo, 2))
print("6. Reporte adicional:")
print("M = 10")
print("cuantas veces cambiaste de material =", cambios)
print("consumo energetico total estimado (kWh) =", round(consumo, 2))
print("K = 3")