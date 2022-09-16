# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 16:49:05 2022

@author: Julián
"""
import random
def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6)) 
    
    return(tirada)
tirar()
def es_generala(tirada):
    for dado in tirada:
        if dado!=tirada[0]:
            return False
            break
            
    return(True)
        
es_generala(tirar())
N = 1000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')

def prob_generala(N):
    generalas=0
    for repeticion in range(N):
        tirada=tirar()
        intentos=0
        for intentos in range(3):
            cuenta={i:tirada.count(i) for i in tirada}
            posicion=list(cuenta.values()).index(max(cuenta.values()))
            dado_elegido=list(cuenta.keys())[posicion]
            for dado in tirada:
                if dado!=dado_elegido:
                    dado_nuevo=random.randint(1,6)
                    tirada.remove(dado)
                    tirada.append(dado_nuevo)
            if es_generala(tirada):
                generalas+=1
                break
            intentos+=1
        # print(intentos)
    proba=generalas/N
    print(f'La probabilidad de sacar una generala con tres tiros es de {proba*100:.2f}%')
    return (proba)
prob_generala(100000)
#%%
# en esta celda propongo que, en caso de no obtener ninguna repetición
# no sé probabilidad ni estadística así que andá a chequear que esto tiene
# sentido
def prob_generala_2(N):
    generalas=0
    for repeticion in range(N):
        tirada=tirar()
        tiradas_totales=1
        cuenta={i:tirada.count(i) for i in tirada}
        def elegir_estrategia(tirada):
            cuenta={i:tirada.count(i) for i in tirada}
            if max(cuenta.values())==1:
                estrategia='A'
            else:
                estrategia='B'
            return(estrategia)
        estrategia=elegir_estrategia(tirada)
        while tiradas_totales<=2 and estrategia=='A':
            tirada=tirar()
            estrategia=elegir_estrategia(tirada)
            if es_generala(tirada):
                generalas+=1
            tiradas_totales+=1
                
        if estrategia=='B':
            while tiradas_totales<=2:
                cuenta={i:tirada.count(i) for i in tirada}
                posicion=list(cuenta.values()).index(max(cuenta.values()))
                dado_elegido=list(cuenta.keys())[posicion]
                for dado in tirada:
                    if dado!=dado_elegido:
                        dado_nuevo=random.randint(1,6)
                        tirada.remove(dado)
                        tirada.append(dado_nuevo)
                if es_generala(tirada): 
                    generalas+=1
                    break
                tiradas_totales+=1

            
        # print(tiradas_totales)
    proba=generalas/N
    print('La probabilidad de sacar una generala con tres tiros')
    print(f'cambiando todos los dados si no hay coincidencias es de {proba*100:.2f}%')
    return (proba)
n=10000
prob_generala(n)
prob_generala_2(n)