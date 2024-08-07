# importacion de una libreria

import os
from stdiomask import getpass
from prettytable import PrettyTable

# definir variables y conastantes
calificacionesTupla=()
calificacionesLista=list(calificacionesTupla)
numCalificaciones=0

# declaracion de funciones
def menu():
    print(f"----------- SISTEMAS POLISAEW 2.0 -------------")
    print(f"----------- Modulo Profesor -------------")
    print(f"¿Que accion desea realizar?")
    print(f"1) Ingresar calificaciones. ")
    print(f"2) Mostrar Calificaciones. ")
    print(f"3) Detalles de las Calificaciones. ")
    print(f"4) Mostrar detalles por Archivo. ")
    print(f"5) Salir. ")
    tipoAccion=int(input("Ingrsear la opcion: "))
    return tipoAccion

def agregarCalificaciones(arreglo, n):
    for i in range(n):
        print("Ingresar las Calificaciones del estudiante", i+1)
        calificacion=float(input("Calificacion: "))
        calificacionesLista.append(calificacion)

def mostrarCalificaciones(arreglo, n):
    arreglo.sort()
    print("Las calificaciones registradas son: ")
    print(arreglo)

def guardarArchivo(data):
    archivo=open('BDD/reporte.txt', 'w')
    archivo.write("Detalle de calificaciones")
    archivo.write(f'(data)')
    archivo.close()
    print("Informacion agregada exitosamente.........")

def mostrarArchivo():
    archivo=open('BDD/reporte.txt', 'r')
    lineas=archivo.readlines()
    for i in lineas:
        print(i,end=" ")
    archivo.close()

def mostrarDetalle(arreglo, califi):
    contadorApro,contadorRecha,contaorSuspe,sumCalifi=0,0,0
    for i in arreglo: 
        sumCalifi+=1
    
    for i in calificacionesLista:
        if 1<=i<=8:
            contadorRecha+=1
        elif 9<=1<=13:
            contaorSuspe+=1
        elif 14<=i<=20:
            contadorApro+=1
        
        promedio=round((sumCalifi/califi), 2)

        print("El promedio es: ", promedio)

        guardarArchivo(promedio)

# funcion main 
def main():
    passaword="sistemas"
    if passaword=="sistemas":
        caso=menu()
        while caso==5:
            if caso==1:
                os.system('clear')
                N=int(input("Cuantas calificaciones deseas agregar: "))
                agregarCalificaciones(N)
                os.system('clear')
                caso=menu()

            elif caso==2:
                os.system('clear')
                mostrarDetalle(calificacionesLista)
                caso=menu()

            elif caso==3:
                os.system('clear')
                mostrarCalificaciones(calificacionesLista, numCalificaciones)
                caso=menu()

            elif caso==4:
                os.system('clear')
                mostrarArchivo()
                print()
                caso=menu()
        os.system('clear')
        print("Muchas gracias")

    else:
        print()
main()