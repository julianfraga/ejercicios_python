# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:20:05 2022

@author: Julián
"""

from bbin import busqueda_binaria_comps
from bseq import busqueda_secuencial_comps
import matplotlib.pyplot as plt
import random
import numpy as np

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)

def promedio_funcion(funcion, lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += funcion(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom


def graficar_bbin_vs_bseq(m=10000, k=1000, n = 100, scale='log'):
    largos = np.arange(256) + 1 # estos son los largos de listas que voy a usar
    comps_promedio_sec = np.zeros(256)
    comps_promedio_bin = np.zeros(256)# aca guardo el promedio de comparaciones sobre una lista de largo i, para i entre 1 y 256.
    for i, n in enumerate(largos):
        lista = generar_lista(n, m) # genero lista de largo n
        comps_promedio_bin[i] = promedio_funcion(busqueda_binaria_comps,lista,  m, k)
        comps_promedio_sec[i] = promedio_funcion(busqueda_secuencial_comps,lista,  m, k)
    plt.clf()
    plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
    plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
    plt.xlabel("Largo de la lista")
    plt.ylabel("Cantidad de comparaciones")
    plt.title("Complejidad de la Búsqueda")
    plt.xscale(scale)
    plt.yscale(scale)
    plt.legend()
    plt.show()
 
graficar_bbin_vs_bseq()
# ahora grafico largos de listas contra operaciones promedio de búsqueda.
# graficar_bbin_vs_bseq(m, k, scale='log')