# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:50:02 2022

@author: Julián

Los ejercicios adicionales me gustaría presentarlos luego si hay posibilidad
Me resultaron interesantes pero por falta de tiempo no los voy a hacer ahora
"""
import numpy as np
import random as rn

# Ejercicios 6.13-6.16
def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(album, figus_total=670):
    return(len(np.nonzero(album)[0])!=figus_total)

def comprar_figu(figus_total):
    return(rn.randint(0, figus_total-1))

def cuantas_figus(figus_total):
    album=crear_album(figus_total)    
    while album_incompleto(album, figus_total):
        figurita=comprar_figu(figus_total)
        album[figurita]+=1
    figuritas_acumuladas=sum(album)
    # print(f'Se compraron {figuritas_acumuladas} figus sueltas para llenar el album')
    return(figuritas_acumuladas)
#%%
# ejercicio 6.17 hecho con numpy y comprensión de listas
n=1000
resultados=np.empty(n)
resultados_lista=[]
for i in range(n):
    x=cuantas_figus(6)
    resultados[i]=x
    resultados_lista.append(x)
    
compra_media=np.mean(resultados)
compra_media_listas=sum(resultados_lista)/n
#%%
# Ejercicio 6.18
def experimento_figus(n_repeticiones, figus_total):
    resultados=np.empty(n_repeticiones)
    for i in range(n_repeticiones):
        x=cuantas_figus(figus_total)
        resultados[i]=x  
    compra_media=np.mean(resultados)
    return compra_media

n_repeticiones=100
figus_total=670
de_a_una=experimento_figus(n_repeticiones, figus_total)
#%%
# Ejercicios 6.19-6.22
def comprar_paquete(figus_total, figus_paquete):
    paquete=[]
    for i in range(figus_paquete):
        paquete.append(rn.randint(0,figus_total-1))
    return paquete
comprar_paquete(670, 5)
def cuantos_paquetes(figus_total=670, figus_paquete=5):
    album=crear_album(figus_total)   
    paquetes_comprados=0
    while album_incompleto(album, figus_total):
        paquete=comprar_paquete(figus_total, figus_paquete)
        for figurita in paquete:
            album[figurita]+=1
    
        paquetes_comprados+=1
    return(paquetes_comprados)

def experimento_paquetes(n_repeticiones=1000, figus_total=670, std=False):
    resultados=np.empty(n_repeticiones)
    for i in range(n_repeticiones):
        x=cuantos_paquetes(figus_total)
        resultados[i]=x  
    compra_media=np.mean(resultados)
    desviacion=np.std(resultados)
    if std==True:
        return (compra_media, desviacion)
    else:
        return(compra_media)
paquetes, std =experimento_paquetes(std=True)
print(f'En promedio hay que comprar {int(paquetes)} paquetes para llenar el álbum')
print(f'A $150 por paquete, serían entre ${150*int(paquetes-std)} y ${150*int(paquetes+std)} para el 68% de los mortales')
print('')
print('MercadoPago no funciona por el momento')
print('Sólo efectivo y con cambio por favor.')
print('Gracias')

import matplotlib.pyplot as plt
def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
