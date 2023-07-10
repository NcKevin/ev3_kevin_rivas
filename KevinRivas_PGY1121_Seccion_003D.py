
import os
import time as t
import msvcrt as m

numero_platinum = list(range(0,20))
cantidad_platinum = 0
monto_platinum = 0

numero_gold = list(range(21,50))
cantidad_gold = 0
monto_gold= 0 

numero_silver = list(range(51,100))
cantidad_silver = 0
monto_silver = 0

asist = []
puest = []

contador = 1
for a in range(10):
    puest_esce = []
    for b in range(10):
        puest_esce.append(contador)
        contador+=1
        puest.append(puest_esce)

def limpiapant(seg):
    print("CARGANDO...")
    t.sleep(seg)
    os.system("cls")

def inicio():
    print("---|Bienvenido a la venta de entradas para el concierto VIP de 'MICHAEL JAM|---")
    
    print("---|RECUERDA, forma exclusiva solo para 100 asistentes|---")
    t.sleep(2)

def menu():
    print("-|*******************************|-")
    print("-|-    CONCIERTO MICHAEL JAM    -|-")
    print("-|*******************************|-")
    print("-|-            -MENU-           -|-")
    print("-|-*****************************-|-")
    print("-|-1.COMPRAR ENTRADAS           -|-")
    print("-|-2.MOSTRAR UBICACIONS DISP.   -|-")
    print("-|-3.VER LISTADO DE ASISTENTES  -|-")
    print("-|-4.MOSTRAR GANANCIAS TOTALES  -|-")
    print("-|-5.SALIR                      -|-")
    op=int(input("Selecciones una opcion por favor:\t"))
    return op

def esce():
    print("*|*---------------------*|*")
    print("*|*      ESCENARIO      *|*")
    print("*|*---------------------*|*")
    for fila in puest:
        print(fila)


def comp_asiento(asiento):
    global cantidad_platinum
    global cantidad_gold
    global cantidad_silver
    global monto_platinum
    global monto_gold
    global monto_silver

    if asiento in numero_platinum:
        cantidad_platinum = cantidad_platinum + 1
        monto_platinum = monto_platinum + 120000
    elif asiento in numero_gold:
        cantidad_gold = cantidad_gold + 1
        monto_gold = monto_gold + 80000
    elif asiento in numero_silver:
        cantidad_silver = cantidad_silver + 1
        monto_silver = monto_silver + 50000

def asiento_ocup(numero):
    contador = 1
    lugar = False
    for fila in puest:
        if (numero in fila):
            lugar = True
    if not lugar:
        print("NO Disponible")
        return True
    for a in puest:
        for b in a:
            if contador==numero and b == 'X':
                return True
    return False

def entrada():
    limpiapant(1.5)
    cantidad_entra = int(input("Cantidad de ENTRADAS a comprar:\t"))
    min=1
    max=3
    while (cantidad_entra<min) or (cantidad_entra>max):
        if cantidad_entra<min:
            cantidad_entra = int(input("DEBE COMPRAR AUNQUE SEA 1na ENTRADA"))
        elif cantidad_entra>max:
            cantidad_entra = int(input("NO PUEDE COMPRAR MAS DE 3 ENTRADAS"))
    esce()
    
    for a in range(cantidad_entra):
        print("")
        asiento = int(input("ASIENTO/S a comprar:\t"))
        while asiento_ocup(asiento):
            asiento = int(input("ASIENTO/S a comprar:\t"))
        ocupado(asiento)
        comp_asiento(asiento)
        
        while True:
            rut_asist = int(input("Ingrese su RUT(SOLO NUMEROS):\t"))
            if len(rut_asist)>9:
                break
            else:
                print("Ingrese el RUT de forma Correcta")

        asist.append(rut_asist)
        print("ENTRADA COMPRADA!")
        limpiapant(3)
        print("Presione cualquier tecla para continuar...")
        m.getch
        limpiapant(0)

def ocupado(asiento):
    for x,a in enumerate(puest):
        for x2,b in enumerate(a):
            if b==asiento:
                puest[x][x2]='X'

def asistente():
    print("-|-**************************-|-")
    print("-|-        ASISTENTES        -|-")
    print("-|-**************************-|-")
    for asist in asist:
        print(asist)
        print("-|-**************************-|-")
        print("-|Presione cualquier tecla para continuar-|")
        m.getch
        limpiapant(1)

def ganancia():
    
    print("-|-***************************************-|-")
    print("-|-               GANANCIAS               -|-")
    print("-|-***************************************-|-")

    print("PLATINUM")
    print("CANTIDAD: ", cantidad_platinum)
    print("MONTO: "   , monto_platinum)

    print("GOLD")
    print("CANTIDAD: ", cantidad_gold)
    print("MONTO: "   , monto_gold)

    print("SILVER")
    print("CANTIDAD:" ,cantidad_silver)
    print("MONTO:"    ,monto_silver)
    print("-|-***************************************-|-")
    total = monto_gold + monto_platinum + monto_silver
    print(f"-|-GANANCIAS TOTALES = {total}            -|-")
    print("-|-***************************************-|-")
    print("-|-Presione cualquier tecla para continuar-|-")
    m.getch()
    limpiapant(1)


while True:
    try:
        os.system("cls")
        
        inicio()
        
        op=menu()
        if op == 1:
            entrada()
        elif op == 2:
            esce()
        elif op == 3:
            asistente()
        elif op == 4:
            ganancia()
        elif op == 5:
            print(f"Gracia por su compra! Fecha de la Compra: {t.localtime().tm_mday}/{t.localtime().tm_mon}/{t.localtime().tm_year}")
            print("Saliendo del Sistema...")
            limpiapant(3)
            for i in range (3,0,-1):
                print(f"Saliendo en {i}")
                limpiapant(1)
            break
        else:
            print("Opcion Incorrecta")
    
    except:
        print("ERROR Inesperado")