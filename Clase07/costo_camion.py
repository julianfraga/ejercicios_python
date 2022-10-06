# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:17:02 2022

@author: Julián
"""
import informe_funciones as info
# archivoCamion='../Data/camion.csv'
def costo_camion(archivo):
    costo_total=0
    lista=info.leer_camion(archivo)
    for i in range(len(lista)):
        costo_total+=lista[i]['cajones']*lista[i]['precio']
    print(f'El costo total es de ${costo_total}')
    return(costo_total)

# costo_camion(archivoCamion)
