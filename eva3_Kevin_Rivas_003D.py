import time as t
import os
import random as r
import msvcrt as m

cliente=[]



def limpiapant():
    t.sleep(1.5)
    print("CARGANDO...")
    os.system("cls")



def menu():
    print("1.|REGISTRO/S del/os Cliente/s|\n")
    print("2.|BUSCAR POR RUT|\n")
    print("3.|REPORTE SEGUN RENTA|\n")
    print("4.|SALIR|\n")
    opcion=int(input("Seleccione una opcion:\t"))
    return opcion

def lista_cliente():
    for lista in cliente:
        for cliente in lista:
            print(cliente)
        print("|-----------------|")



def registro():
    
    while True:
        rut=input("Ingrese RUT :\t")
        if (len(rut)==9) and rut.isdigit():
            break
        else:
            print("INGRESE RUT VALIDO")
    while True:
        
        nom_cliente=input("Ingrese NOMBRE :\t")
        if len(nom_cliente)<1:
            print("DEBE INGRESAR NOMBRE")
        else:
            break
            
    while True:
        proyecto=int(input("Ingrese el Proyecto que desea comprar: |1.'VIVE SANTIAGO'= 'VS', 2.VIVE LA FLORIDA= 'VF', 3.VIVE ÑUÑOA= 'VÑ' "))
        if proyecto==1:
            nom_pro = "VS"
            print("PROYECTO : VIVE SANTIAGO")
            break
        elif proyecto == 2:
            nom_pro = "VF"
            print("PROYECTO : VIVE LA FLORIDA")
            break
        elif proyecto == 3:
            nom_pro = "VÑ"
            print("PROYECTO: VIVE ÑUÑOA")
            break
        renta_men = r.randrange(400000,9999999)
        cliente[rut,nom_cliente,nom_pro,renta_men]
        cliente.append(cliente)
    limpiapant()
    print("REGISTRO COMPLETADO")
    



def buscar(rut):
    i=1
    for lista in cliente:
        if lista[0] == rut:
            print(f"RUT Cliente: {lista[0]} ")
            print(f"Nombre Cliente: {lista[1]}")
            print(f"Proyecto Comprado: {lista[2]}")
            print(f"Renta Mensual : {lista[3]}")
            
            i=0
    
    if i==1:
        print("NO SE ENCONTRO CLIENTE")
        limpiapant
    print("Presione Cualquier tecla para continuar")
    m.getch()
    limpiapant()



def reporte_ren():
    cont=0
    print("|-----REPORTE RENTA-----|")
    for lista in cliente:
        if lista[3] >= 900000:
            cont+=1
            print(f"RUT CLIENTE: {lista[0]} ")
            print(f"Nombre Cliente: {lista[1]}\n")
            print(f"RENTA MENSUAL : {lista[3]}")
            print(f"Proyecto Elegido: {lista[2]}")
            print(f"Puede acceder aun Dpt de UF {r.randrange(2500,3700)}\n")
            print(f"Se generaron {cont} reportes")



#Sintaxis BASE

os.system("cls")

while True:
    try:
        opcion= menu()
        
        if opcion == 1:
            registro()
        elif opcion == 2:
            while True:
                rut = input("Ingrese Rut del Cliente: \t")
                if (len(rut)==9) and rut.isdigit():
                    buscar(rut)
                    break
                else:
                    print("RUT INVALIDO")
        
        elif opcion == 3:
            reporte_ren()

        
        
        elif opcion == 4:
            for i in range(5,0,-1):
                print(f"Saliendo en {i}")
                limpiapant()
            break
        else:
            print("Opcion invalida")
        
        
    except:
        print("ERROR INESPERADO")
        