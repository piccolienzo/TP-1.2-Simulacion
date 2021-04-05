import random
import collections
import numpy as np 
from scipy import stats 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#jugadas


def main():
    
    capital_jugador = int(valid_input(0,50,"Con cuanto inicial dinero desea jugar? ","Error: Ingrese una opcion valida "))
    ficha = valid_input(1,5,"Que ficha desea jugar?: "+ str(fichas), "Error: Ingrese valor de ficha valido")
    ficha = fichas[ficha]
    
    
    jugada = valid_input(1,7,"Que tipo de jugada realizará?\n1. Pleno\n2. Docenas\n3. Filas\n4. Rojo\n5. Negro\n6. Par\n7. Impar","Error: Seleccione jugada válida")

    capital_jugador-=ficha 
    if jugada == 1:
        apuesta = valid_input(0,36,"Ingrese jugada al pleno","Error: Ingrese una opcion valida de ruleta")
        jugar(ficha,[apuesta],2,capital_jugador)
    
    elif jugada == 2:
        apuesta = valid_input(1,3,"Ingrese docena a apostar (1,2,3)","Error: Ingrese una opcion valida de ruleta")
        jugar(ficha,[docenas[apuesta]],2,capital_jugador)
    
    elif jugada == 3:
        apuesta = valid_input(1,3,"Ingrese filas a apostar (1,2,3)","Error: Ingrese una opcion valida de ruleta")
        jugar(ficha,[filas[apuesta]],2,capital_jugador)
    
    elif jugada == 4:
        print("Usted aposto a ROJO")
        jugar(ficha,rojo,2,capital_jugador)
    elif jugada == 5:
        print("Usted aposto a NEGRO")
        jugar(ficha,negro,2,capital_jugador)
    elif jugada == 6:
        print("Usted aposto a PAR")
        jugar(ficha,pares,2,capital_jugador)
    elif jugada == 7:
        print("Usted aposto a IMPAR")
        jugar(ficha,impares,2,capital_jugador)
    else:
        print('error')


def jugar(_ficha, _apuesta, _multiplicador,capital_jugador):      
    nro_ruleta = getRandomInt()
    gano = False
    if nro_ruleta in _apuesta:
        print("felicidades pa ganaste $"+ str(_ficha * _multiplicador))
        print("saldo actual: $"+str(capital_jugador + _ficha * _multiplicador))

    else:
        print("perdiste paaaaaa -$"+str(_ficha))
        print("saldo actual: $"+str(capital_jugador))   
    
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
   

MIN=0
MAX=36

plenos =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
docenas = [[0],[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
filas = [[0],[1,4,7,10,13,16,19,22,25,28,31,34],[2,5,8,11,14,17,20,23,26,29,32,25],[3,6,9,12,15,18,21,24,27,30,33,36]]
rojo = [1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
negro = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
impares = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]


fichas = {1:5,2:10,3:25,4:50,5:100}


capital_caja = 100000
main()