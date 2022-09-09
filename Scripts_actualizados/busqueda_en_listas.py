# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:16:46 2022

@author: Julián
"""

def buscar_u_elemento(lista, e):
    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
    return pos

def buscar_n_elemento(lista, e):
    contador=0
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            contador+=1
    return (contador)

def maximo(lista):
    '''Devuelve el máximo de una lista. Puede estar vacía y tener
    números negativos.
    '''
    if lista:
        m = lista[0] #inicializo m con el primer elemento, arbitrariamente
        for e in lista: # Recorro la lista y voy guardando el mayor
            if e>m:
                m=e
        return m
    else:
        return('La lista está vacía')
    
maximo([-5,-4])
maximo([-5,10, -2])
maximo([])
