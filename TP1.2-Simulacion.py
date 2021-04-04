import random
import collections
import numpy as np 
from scipy import stats 
import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

#jugadas
MIN=0
MAX=36

docenas = [[0],[1,2,3,4,5,6,7,8,9,10,11,12],[13,14,15,16,17,18,19,20,21,22,23,24],[25,26,27,28,29,30,31,32,33,34,35,36]]
filas = [[0],[1,4,7,10,13,16,19,22,25,28,31,34],[2,5,8,11,14,17,20,23,26,29,32,25],[3,6,9,12,15,18,21,24,27,30,33,36]]
rojo = [1,3,5,7,9,12,14,16,18,21,23,25,27,30,32,34,36]
negro = [2,4,6,8,10,11,13,15,17,19,20,22,24,26,28,29,31,33,35]
pares = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
impares = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]


fichas = {1:10,2:25,3:50,4:100}

capital_jugador = 0
capital_caja = 100000

def main():
    capital_jugador = valid_input(0,50,"Con cuanto inicial dinero desea jugar? ","Error: Ingrese una opcion valida ")
    ficha = valid_input(1,5,"Que ficha desea jugar?: "+ str(fichas), "Error: Ingrese valor de ficha valido")
    ficha = fichas[ficha]

    jugada = valid_input(1,7,"Que tipo de jugada realizará?\n1. Pleno\n2. Docenas\n3. filas\n4. Rojo\n5. Negro\n6. Par\n7. Impar","Error: Seleccione jugada válida")

    
    print(ficha)
    



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

#Retorna una Lista de números aleatorios
"""def getRandomIntList():
    randomList = []
    for x in range(MIN,SIZE):
        randomList.append(getRandomInt())
                  
    return randomList"""

    
main()