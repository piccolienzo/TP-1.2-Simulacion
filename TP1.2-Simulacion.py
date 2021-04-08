import random
import collections
import numpy as np 
from scipy import stats 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches




def juego():  
    
    global capital_jugador
    
    global capital_caja
    global ganadas

    
    capital_jugador = int(valid_input(500,10000,"Con cuanto inicial dinero desea jugar? ","Error: Ingrese una opcion valida (500 a 10000) "))
    estrategia = int(valid_input(1,2,"Que estrategia desea jugar 1- D'Alembert 2-Martin Gala ","Error: Ingrese una estrategia valida "))
    callback = 0
    if(estrategia == 1):
        callback = d_alembert
    else:
        callback = martin_gala

    ficha = valid_input(1,5,"Que ficha desea jugar?: "+ str(fichas), "Error: Ingrese valor de ficha valido")
    
    ficha = fichas[ficha]
    
    
    jugada = valid_input(1,7,"Que tipo de jugada realizará?\n1. Pleno\n2. Docenas\n3. Filas\n4. Rojo\n5. Negro\n6. Par\n7. Impar","Error: Seleccione jugada válida")

    
    if jugada == 1:
        apuesta = valid_input(0,36,"Ingrese jugada al pleno","Error: Ingrese una opcion valida de ruleta")
       
        jugar(ficha, ficha, [apuesta], 36, callback,0)
    
    elif jugada == 2:
        apuesta = valid_input(1,3,"Ingrese docena a apostar [1,2,3]","Error: Ingrese una opcion valida de ruleta")
        
        jugar(ficha, ficha, [docenas[apuesta]], 3, callback,0)
    
    elif jugada == 3:
        apuesta = valid_input(1,3,"Ingrese filas a apostar [1,2,3]","Error: Ingrese una opcion valida de ruleta")     
        jugar(ficha, ficha, [filas[apuesta]], 3, callback,0)
    
    elif jugada == 4:
        print("Usted aposto a ROJO")
        jugar(ficha, ficha, rojos, 2, callback,0)

    elif jugada == 5:
        print("Usted aposto a NEGRO")
        jugar(ficha, ficha, negros, 2, callback,0)

    elif jugada == 6:
        print("Usted aposto a PAR")
        
        jugar(ficha, ficha, pares, 2, callback,0)

    elif jugada == 7:
        print("Usted aposto a IMPAR")
        jugar(ficha, ficha, impares, 2, callback,0)

    else:
        print('error')
    


def d_alembert(_ficha,_apuesta):
    var = _apuesta + _ficha   
    return var

def martin_gala(_ficha,apuesta):
    var = apuesta * 2
    return var


def jugar(_apostado,_ficha, _apuesta, _multiplicador, estrategia, contador): 
    global capital_jugador
    global capital_caja
    global ganadas
    #Ficha: valor de la ficha:5 #Apuesta: numeros donde debe salir:[5,40,30] #capital: 500 
    contador += 1
    nro_ruleta = getRandomInt()
    print("capital caja antes de jugar: $"+str(capital_caja))
    gano = False
   
    ##Para infinito (infinito == True and contador < infi_limit)

    if ((capital_jugador >= _apostado and capital_caja >= _apostado)):
        #puede jugar
        print("en juego hay $"+str(_apostado))
        
        flujo_caja.append(capital_caja)
        flujo_jugador.append(capital_jugador)

        capital_jugador -=  _apostado
        capital_caja += _apostado

        print("saldo actual:"+str(capital_jugador))
        if nro_ruleta in _apuesta:
            #ganó
            ganancia = _apostado * _multiplicador
            capital_jugador += ganancia
            capital_caja-=ganancia
            #suponemos que no cambia la apuesta
            print("gano: $"+str(ganancia)+" capital actual: $"+str(capital_jugador))
            ganadas.append(1)
            jugadas.append(contador)
            jugar(_ficha,_ficha,_apuesta,_multiplicador,estrategia,contador)
                    
        else:
            #perdio            
            print("perdio: $"+str(_apostado)+" capital actual: $"+str(capital_jugador))

            ganadas.append(0)
            jugadas.append(contador)
            jugar(estrategia(_ficha,_apostado),_ficha,_apuesta,_multiplicador,estrategia,contador)
            
    else:
        #no puede juegar mas
        print("capital final: " + str(capital_jugador))
        print("perdiste en "+ str(contador)+ " veces")
        print("capital caja: $"+str(capital_caja))

    return gano

 
def valid_input(min,max,message,error_message):
    f = False
    player_input = ""
    print(message)
    while(f==False):
        player_input = int(input())
        if(player_input >= min and player_input <= max):
            f = True
        else:
            print(error_message)  
    return player_input

#Retorna un entero aleatorio entre el minimo y el máximo
def getRandomInt():
    number = random.randint(MIN,MAX)
    return number
   

def plotVars():
    
    #FLUJO DE CAJA
    plt.figure(figsize=(18,10))
    plt.plot(flujo_caja) 
    plt.title("Flujo Caja")
        
    #blue_patch = mpatches.Patch(color='blue', label='Promedio de la muestra')
    #orange_patch = mpatches.Patch(color='orange', label='Promedio esperado')
    #plt.legend(handles=[blue_patch,orange_patch])
    plt.xlabel('Jugada')
    plt.ylabel('Dinero en caja')

    plt.ylim(min(flujo_caja),max(flujo_caja))
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.savefig("FLUJO_CAJA"+str(EXT),bbox_inches='tight')
    plt.show()
    plt.close()



    #DINERO JUGADOR
    plt.figure(figsize=(18,10))
    plt.plot(flujo_jugador) 
    plt.title("Dinero del jugador")
     
    plt.xlabel('Tirada')
    plt.ylabel('Dinero en jugador')    

    plt.ticklabel_format(useOffset=False, style='plain')
    plt.savefig("DINERO_JUGADOR"+str(EXT),bbox_inches='tight')
    plt.show()
    plt.close()


    frec_relativa = []
    cont = 0
    for index in range(len(jugadas)):
        if ganadas[index] == 1:
            cont += 1
            frec_relativa.append(cont/index)
        else:
            frec_relativa.append(0)
    
    plt.figure(figsize=(18,10))
    
    plt.bar(jugadas,frec_relativa)
    
    plt.title("Frecuencias relativas para "+str(len(jugadas))+ " tiradas")
    plt.xlabel("Jugadas")
    plt.ylabel("Frecuencia relativa ")
    
    plt.savefig("FRECUENCIAS_RELATIVAS_"+str(EXT),bbox_inches='tight')
    plt.show()
    plt.close()


   

MIN = 0
MAX = 36


plenos =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
docenas = [[0],[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
filas = [[0],[1,4,7,10,13,16,19,22,25,28,31,34],[2,5,8,11,14,17,20,23,26,29,32,25],[3,6,9,12,15,18,21,24,27,30,33,36]]
rojos = [1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
negros = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
impares = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]


fichas = {1:5,2:10,3:25,4:50,5:100}

flujos_de_caja = []
flujos_jugador = []


flujo_caja = []
flujo_jugador = []

ganadas = []
jugadas = []

infi_limit = 200
infinito = True

capital_caja = 1000000
capital_jugador = 0
EXT = ".svg"


juego()
plotVars()



