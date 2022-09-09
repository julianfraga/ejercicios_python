# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:50:16 2022

@author: Julián
"""

def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e)
    return invertida

lista=['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
print('Entra ', lista)
print('Sale ', invertir_lista(lista))