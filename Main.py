from Package_Input.Funciones_Input import *
from Package_Matrices.Matrices import *
from random import *
from os import system

recaudaciones = crear_matriz(3,5,0)
legajos=[0] * 15
for i in range(15):
    legajos[i] = randint(1000,9999)
print(legajos)
menu=True
while menu:
    opcion = input(
    "a. Cargar recaudación (el chofer se debe identificar con su legajo)\n"
    "b. Mostrar todas las recaudaciones (por línea y coche)\n"
    "c. Calcular y mostrar la recaudación por línea\n"
    "d. Calcular y mostrar la recaudación por coche\n"
    "e. Calcular y mostrar la recaudación total\n"
    "f. Salir\n"
    "Elija una opción: ")
    match opcion:
        case "a":
            legajo = get_int("Ingrese su legajo: ",1000,9999,"Incorrecto, Reingresar: ")
            for i in range(len(legajos)):
                if legajo == legajos[i]:
                    linea = get_int("Ingrese la linea correspondiente: ",1,3,"Linea inexistente, Reingrese la linea: ")
                    coche = get_int("Ingrese el coche correspondiente: ", 1, 5, "Coche inexsistente, Reingrese el coche: ")
                    monto = get_int("Ingrese el monto a acreditar: ", 1000,10000,"Monto fuera de rango, Reintente: ")
                    ingresar_monto(recaudaciones,linea,coche,monto)
        case "b":
            mostrar_matriz(recaudaciones)
        case "c":
            matriz_filas = calcular_recaudacion_linea(recaudaciones)
            for i in range(len(matriz_filas)):
                print(f"La recaudación de la línea {i+1} ha sido {matriz_filas[i]}")
        case "d":
            matriz_coches = calcular_recaudacion_coche(recaudaciones)
            for i in range(len(matriz_coches)):
                print(f"La recaudación del coche {i+1} ha sido {matriz_coches[i]}")
        case "e":
            total=calcular_recaudacion_total(recaudaciones)
            print(f"La recaudacion total ha sido {total}")
        case"f":
            menu= False
    system("pause")
    system("cls")
        
