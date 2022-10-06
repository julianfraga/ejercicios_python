# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 14:24:53 2022

@author: Julián
"""
import fileparse as fp
import csv
f_camion='../Data/camion.csv'
fp.parse_csv(f_camion, types=[str, int, float])
def leer_camion(nombre_archivo):
    camion = fp.parse_csv(nombre_archivo, types=[str, int, float])
    return camion
def leer_precios(nombre_archivo):
    listaDeTuplas=fp.parse_csv(nombre_archivo, types=[str,float], has_headers=False)
    precios= [{listaDeTuplas[i][0]:listaDeTuplas[i][1]} for i in range(len(listaDeTuplas))]
    return precios

def hacer_informe(camion, precios):
    lista = []
    for lote in camion:
        precio_venta = precios[lote['nombre']]
        cambio = precio_venta - lote['precio'] 
        t = (lote['nombre'], lote['cajones'], lote['precio'], cambio)
        lista.append(t)
    return lista


def imprimir_informe(nombre_archivo1, nombre_archivo2):
    ''' imprime el informe '''
    camion = leer_camion(nombre_archivo1)
    precios = leer_precios(nombre_archivo2)
    informe = hacer_informe(camion, precios)

    print('    Nombre    Cajones     Precio     Cambio')
    print('---------- ---------- ---------- ----------')
    for nombre, cajones, precio, cambio in informe:
        precio = f'${precio}'
        print(f'{nombre:>10s} {cajones:>10d} {precio:>10s} {cambio:>10.2f}')
    return
    

def informe_camion(nombreArchivoCamion, nombreArchivoPrecios):
    imprimir_informe(nombreArchivoCamion, nombreArchivoPrecios)

#%%

# camion = leer_camion('../Data/camion.csv')
# precios = leer_precios('../Data/precios.csv')
# informe = hacer_informe(camion, precios)

# informe_camion('../Data/camion.csv', '../Data/precios.csv')
# informe_camion('../Data/camion2.csv', '../Data/precios.csv')
# files = ['../Data/camion.csv', '../Data/camion2.csv']
# for name in files:
#     print(f'{name:-^43s}')
#     informe_camion(name, '../Data/precios.csv')
#     print()
