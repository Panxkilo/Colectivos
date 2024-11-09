def crear_matriz(filas:int,columnas:int,valor_inicial)->list:
    matriz = []
    for i in range(filas):
        filas = [valor_inicial] * columnas
        matriz = matriz + [filas]
    return matriz

def mostrar_matriz(matriz:list)->None:
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()


def ingresar_monto(matriz:list,linea:int,coche:int,monto:int)->list:
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == matriz[linea-1][coche-1]:
                matriz[linea-1][coche-1] += monto
    return matriz

def calcular_recaudacion_linea(matriz:list):
    matriz_suma_linea = [0] * len(matriz)
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            matriz_suma_linea[fila] = matriz_suma_linea[fila] + matriz[fila][columna]
    return matriz_suma_linea

def calcular_recaudacion_coche(matriz:list):
    matriz_suma_coche = [0] * len(matriz[0])
    for columna in range(len(matriz[0])):
        for fila in range(len(matriz)):
            matriz_suma_coche[columna] = matriz_suma_coche[columna] + matriz[fila][columna]
    return matriz_suma_coche


def calcular_recaudacion_total(matriz):
    acumulador = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            acumulador += matriz[fila][columna]
    return acumulador

